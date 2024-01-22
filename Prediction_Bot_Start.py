import importlib
import os
import sys
import subprocess
import os
import sys
import subprocess
import importlib.util


def run_simulation_script():
    simulation_script = 'bsc_blockchain.py'
    if sys.platform == "win32":
        os.system(f'start cmd /k python {simulation_script}')

def install_and_import(module_name):
    try:
        if importlib.util.find_spec(module_name) is None:
            print(f"{module_name} module installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
        else:
            print(f"{module_name} module already installed.")
        globals()[module_name] = importlib.import_module(module_name)
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {module_name}. Error: {e}")
        sys.exit(1)

def main():
    modules = ['pyfiglet']

    for mod in modules:
        install_and_import(mod)
    import pyfiglet

    header1 = pyfiglet.figlet_format("PancakeSwap", font="standard")
    header2 = pyfiglet.figlet_format("Prediction Bot", font="standard")
    header3 = pyfiglet.figlet_format("v27.1", font="standard")
    
    print("\033[1;36m" + header1 + "\033[0m")
    print("\033[1;36m" + header2 + "\033[0m")
    print("\033[1;36m" + header3 + "\033[0m\n")
    
    run_simulation_script()

if __name__ == "__main__":
    main()
