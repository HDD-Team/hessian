from flet import *
from inference import cheat



def main(page: Page):
    page.title = 'Hessian'
    page.scroll = "auto"
    page.bgcolor = '#F2F2F2'
    m_col = '#243B55'
    a_col = '#4D9DE0'



    def inf(e):
        f:str = str(func.value)
        f = f.replace('^', '**')
        s = []
        for symb in list("qwertyuioplkjhgfdsazxcvbnm"):
            if symb in f:
                s.append(symb)
        s = " ".join(s)
        ans = cheat(f,s)
        text.value=ans
        page.update()



    func = TextField(value="", hint_text='enter the function in python like style', color=m_col, autofocus=True, on_submit=inf)
    text = Text(value='', color=m_col, size=30)

    upper = Container(
        Row(
            [
                Container(width=20),
                Text('Hessian', color=m_col, size=30)
            ],
            height=40,
            expand=True,
        ),
        bgcolor=a_col,
        height=80,
        margin=-10,
        border_radius=border_radius.only(0,0,15,15)
    )
    body = Container(
        Row(
            [
                Column(
                    [
                        Container(height=100),
                        func,
                        text,
                    ],
                    #alignment=alignment.center,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    expand=True,
                )
            ],
            expand=True,
            #alignment=alignment.center,
            vertical_alignment=CrossAxisAlignment.CENTER,

        ),
        alignment=alignment.center,
    )

    page.add(upper,body)
    




if __name__ == "__main__":
    app(target=main)
