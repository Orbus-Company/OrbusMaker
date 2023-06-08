import os

def createflet(projectNAME):
    rutaActual = os.getcwd()
    rutaProject = os.path.join(rutaActual,projectNAME)
    os.mkdir(rutaProject)
    
    # CREATE PAGES DIR
    dirNAME = 'pages'          # Invocado, NOMBRE
    rutaProject = os.path.join(rutaActual,projectNAME)
                        #invocado/NOMBRE/pages 
    newDIR = os.path.join(rutaProject, dirNAME)
    os.mkdir(newDIR)
    
    os.chdir(newDIR)
    view1 = open("view1.py", "w")
    view1.write("""\nimport flet as ft\nfrom flet import *\n\ndef _view_():\n\treturn View(\n\t\t'/view1',\n\t\tcontrols=[\n\t\t\tColumn(\n\t\t\t\tcontrols=[\n\t\t\t\t\tRow(\n\t\t\t\t\t\tcontrols=[\n\t\t\t\t\t\t\tFilledButton(\n\t\t\t\t\t\t\t\ttext='View1',\n\t\t\t\t\t\t\t\twidth=100,\n\t\t\t\t\t\t\t\theight=40,\n\t\t\t\t\t\t\t\ton_click=lambda e: e.page.go('/view1'),\n\t\t\t\t\t\t\t),\n\t\t\t\t\t\t\tFilledButton(\n\t\t\t\t\t\t\t\ttext='View2',\n\t\t\t\t\t\t\t\twidth=100,\n\t\t\t\t\t\t\t\theight=40,\n\t\t\t\t\t\t\t\ton_click=lambda e: e.page.go('/view2'),\n\t\t\t\t\t\t\t),\n\t\t\t\t\t\t\tFilledButton(\n\t\t\t\t\t\t\t\ttext='View3',\n\t\t\t\t\t\t\t\twidth=100,\n\t\t\t\t\t\t\t\theight=40,\n\t\t\t\t\t\t\t\ton_click=lambda e: e.page.go('/view3'),\n\t\t\t\t\t\t\t),\n\t\t\t\t\t\t]\n\t\t\t\t\t),\n\t\t\t\t\tft.Divider(thickness=1),\n\t\t\t\t\t# MAIN CONTENT\n\t\t\t\t\tft.Text("View1")\n\t\t\t\t]\n\t\t\t)\n\t\t],\n\t)""")
    view1.close()

    view2 = open("view2.py", "w")
    view2.write("""\nimport flet as ft\nfrom flet import *\n\ndef _view_():\n\treturn View(\n\t\t'/view2',\n\t\tcontrols=[\n\t\t\tColumn(\n\t\t\t\tcontrols=[\n\t\t\t\t\tRow(\n\t\t\t\t\t\tcontrols=[\n\t\t\t\t\t\t\tFilledButton(\n\t\t\t\t\t\t\t\ttext='View1',\n\t\t\t\t\t\t\t\twidth=100,\n\t\t\t\t\t\t\t\theight=40,\n\t\t\t\t\t\t\t\ton_click=lambda e: e.page.go('/view1'),\n\t\t\t\t\t\t\t),\n\t\t\t\t\t\t\tFilledButton(\n\t\t\t\t\t\t\t\ttext='View2',\n\t\t\t\t\t\t\t\twidth=100,\n\t\t\t\t\t\t\t\theight=40,\n\t\t\t\t\t\t\t\ton_click=lambda e: e.page.go('/view2'),\n\t\t\t\t\t\t\t),\n\t\t\t\t\t\t\tFilledButton(\n\t\t\t\t\t\t\t\ttext='View3',\n\t\t\t\t\t\t\t\twidth=100,\n\t\t\t\t\t\t\t\theight=40,\n\t\t\t\t\t\t\t\ton_click=lambda e: e.page.go('/view3'),\n\t\t\t\t\t\t\t),\n\t\t\t\t\t\t]\n\t\t\t\t\t),\n\t\t\t\t\tft.Divider(thickness=1),\n\t\t\t\t\t# MAIN CONTENT\n\t\t\t\t\tft.Text("View2")\n\t\t\t\t]\n\t\t\t)\n\t\t],\n\t)""")
    view2.close()
    
    view3 = open("view3.py", "w")
    view3.write("""\nimport flet as ft\nfrom flet import *\n\ndef _view_():\n\treturn View(\n\t\t'/view3',\n\t\tcontrols=[\n\t\t\tColumn(\n\t\t\t\tcontrols=[\n\t\t\t\t\tRow(\n\t\t\t\t\t\tcontrols=[\n\t\t\t\t\t\t\tFilledButton(\n\t\t\t\t\t\t\t\ttext='View1',\n\t\t\t\t\t\t\t\twidth=100,\n\t\t\t\t\t\t\t\theight=40,\n\t\t\t\t\t\t\t\ton_click=lambda e: e.page.go('/view1'),\n\t\t\t\t\t\t\t),\n\t\t\t\t\t\t\tFilledButton(\n\t\t\t\t\t\t\t\ttext='View2',\n\t\t\t\t\t\t\t\twidth=100,\n\t\t\t\t\t\t\t\theight=40,\n\t\t\t\t\t\t\t\ton_click=lambda e: e.page.go('/view2'),\n\t\t\t\t\t\t\t),\n\t\t\t\t\t\t\tFilledButton(\n\t\t\t\t\t\t\t\ttext='View3',\n\t\t\t\t\t\t\t\twidth=100,\n\t\t\t\t\t\t\t\theight=40,\n\t\t\t\t\t\t\t\ton_click=lambda e: e.page.go('/view3'),\n\t\t\t\t\t\t\t),\n\t\t\t\t\t\t]\n\t\t\t\t\t),\n\t\t\t\t\tft.Divider(thickness=1),\n\t\t\t\t\t# MAIN CONTENT\n\t\t\t\t\tft.Text("View3")\n\t\t\t\t]\n\t\t\t)\n\t\t],\n\t)""")
    view3.close()
    
    # CREATE PUBLIC DIR
    dirNAME = 'public'
    rutaProject = os.path.join(rutaActual,projectNAME)
    newDIR = os.path.join(rutaProject, dirNAME)
    os.mkdir(newDIR)

    # CREATE MAIN.py
    os.chdir(rutaProject)
    main = open("main.py", "w")
    main.write("""\nimport flet as ft\nfrom flet import *\nfrom pages.view1 import _view_ as v1\nfrom pages.view2 import _view_ as v2\nfrom pages.view3 import _view_ as v3\n\ndef main(page: Page):\n\tpage.theme_mode = "dark"\n\tpage.title = 'ORBUS + FLET'\n\tview1 = v1()\n\tview2 = v2()\n\tview3 = v3()\n\tdef route_change(route):\n\t\tpage.views.clear()\n\t\tif page.route == '/view2':\n\t\t\tpage.views.append(view2)\n\t\tif page.route == '/view3':\n\t\t\tpage.views.append(view3)\n\t\tif page.route == '/view1':\n\t\t\tpage.views.append(view1)\n\t\tpage.update()\n\tdef view_pop(view):\n\t\tpage.views.pop()\n\t\ttop_view = page.views[-1]\n\t\tpage.go(top_view.route)\n\tpage.on_route_change = route_change\n\tpage.on_view_pop = view_pop\n\tpage.go(page.route)\n\n\tpage.views.append(view3)\n\tpage.views.append(view2)\n\tpage.views.append(view1)\n\n\tpage.update()\n\nft.app(target=main, assets_dir='assets')\n# ft.app(target=main, assets_dir='assets', port=5000, view=ft.WEB_BROWSER)""")
    main.close()

def FLET():
    projectNAME = input('Ingrese el nombre de su proyecto (flet-app)\n>> ')
    if projectNAME == "":
        projectNAME = 'flet-app'
        createflet(projectNAME)
    else:
        createflet(projectNAME)

if __name__ == "__main__":
    FLET()
