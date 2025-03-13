# jupyter-notebook-wannabe
a tool to substitute jupyter notebook installation for the curricular unit of ANADI (Análise de Dados em Informática, ISEP)

### requirements
- docker

### first steps
- open the script run.sh, with any text editor, and chnage the default path (VOLUME) to the project root directory
- you may want to change the local port (LOCAL_PORT), but it is optional
- you may also change the names of the container and image

### running the script
- after the first steps are completed, run the script with the '-r' flag
- every time you make changes to the main.py you have to run the script with the '-r' flag
> e.g. ./run.sh -r
