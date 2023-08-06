from os.path import join
from myp import MYPReader
from myp import const as myp_const
from typing import List
from ..utils import (
    info_message,
    process_ok,
    process_step,
    create_folder,
    success_message,
    make_compatible,
    hl,
    take_input
)
from .utils import (
    create_app_init_py,
    create_models_py,
    create_forms_py,
    create_routes_py,
    append_app_datas,
)
from ..__main__ import main

@main.command("startapp")
def startapp_command():
    """Create new app inside project"""
    processes:List[str] = []
    process_ok(processes)

    # Taking app name
    app_name:str = make_compatible(take_input("Enter name for app:"))

    # Creating app folder
    prj_name:str = MYPReader().get_data("config").get('PROJECT_NAME', "")
    if not prj_name :
        raise Exception(f"You deleted your project name from {myp_const.filename} file. Please add it.")
    
    process_step(f"Creating {hl(join(prj_name, app_name))} folder...",
                create_folder(join(prj_name, app_name)))
    processes.append(f"Created {hl(join(prj_name, app_name))} folder")
    process_ok(processes)

    # Creating __init__.py
    process_step(f"Creating {hl(join(prj_name, app_name, '__init__.py'))}...",
                create_app_init_py(join(prj_name, app_name)))
    processes.append(f"Created {hl(join(prj_name, app_name, '__init__.py'))}")
    process_ok(processes)

    # Creating templates folder
    process_step(f"Creating {hl(join(prj_name, app_name, 'templates'))} folder...",
                create_folder(join(prj_name, app_name, 'templates')))
    processes.append(f"Created {hl(join(prj_name, app_name, 'templates'))} folder")
    process_ok(processes)
    
    # Creating models.py
    process_step(f"Creating {hl(join(prj_name, app_name, 'models.py'))}...",
                create_models_py(join(prj_name, app_name)))
    processes.append(f"Created {hl(join(prj_name, app_name, 'models.py'))}")
    process_ok(processes)

    # Creating forms.py
    process_step(f"Creating {hl(join(prj_name, app_name, 'forms.py'))}...",
                create_forms_py(join(prj_name, app_name)))
    processes.append(f"Created {hl(join(prj_name, app_name, 'forms.py'))}")
    process_ok(processes)

    # Creating routes.py
    process_step(f"Creating {hl(join(prj_name, app_name, 'routes.py'))}...",
                create_routes_py(prj_name,app_name))
    processes.append(f"Created {hl(join(prj_name, app_name, 'routes.py'))}")
    process_ok(processes)

    # Appending app datas to __init__.py
    process_step(f"Appending {app_name} modules to {hl(join(prj_name, '__init__.py'))}...",
                append_app_datas(prj_name, app_name))
    processes.append(f"Appended {app_name} modules to {hl(join(prj_name, '__init__.py'))}")
    process_ok(processes)

    # Appending app name to myp config
    myp = MYPReader()
    myp_config = myp.get_data("config")
    myp_config['APPS'].append(app_name)
    myp.set_data("config",myp_config)
    myp.write()

    # Output success message
    success_message(f"Successfully created {hl(app_name)}")
    info_message(f"Use {hl('myp start')} to run your application")
