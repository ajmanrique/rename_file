#! /bin/python

import os, glob, shutil, sys

def main(*args):
    os.chdir(args[0])
    print("Buscando archivos...")
    iter_files = glob.glob("**/{}".format(args[1]), recursive=True)
    for f in iter_files:
        print("---------------------------------------------")
        abs_path = os.path.dirname(os.path.abspath(f))
        file_name = os.path.basename(os.path.abspath(f))
        file_bck = "{}.bck".format(file_name)

        print("Crando respaldo de archivo {}".format(file_name))
        shutil.copy(os.path.join(abs_path, file_name), os.path.join(abs_path, file_bck))
        
        print("Renombrando archivo: {}".format(file_name))
        shutil.move(os.path.join(abs_path, file_name), os.path.join(abs_path, args[2]),)

        print("Resultado en directorio: {0} = {1}".format(abs_path, os.listdir(abs_path)))

    print("Archivos tratados: {}".format(len(iter_files)))


if __name__ == "__main__":
    path_base = sys.argv[1]
    file_search = sys.argv[2]
    new_file = sys.argv[3]
    main(path_base, file_search, new_file)