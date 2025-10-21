from tkinter import *
from PIL import Image, ImageTk
import os

class skyguideapp():
    def __init__(self, root):
        self.program = root
        self.program.title("--SPACE VISION --")
        self.program.geometry("500x900")
        self.program.resizable()

        # === Canvas ===
        self.canvas = Canvas(self.program, width=500, height=900, highlightthickness=0, bd=0)
        self.canvas.pack(fill="both", expand=True)
        bg_candidates = [
            "/Users/weiqixuan/Desktop/ddt_work/SPACEVISION_T/assests/backgroundimage.jpg",
            "/Users/weiqixuan/Desktop/ddt_work/SPACEVISION_T/assets/backgroundimage.jpg",
        ]
        bg_path = next((p for p in bg_candidates if os.path.exists(p)), None)
        if bg_path:
            try:
                self.backg_image = Image.open(bg_path).resize((500, 900))
                self.backg_photo = ImageTk.PhotoImage(self.backg_image)
                self.canvas.create_image(0, 0, image=self.backg_photo, anchor="nw")
            except Exception as e:
                self.canvas.create_rectangle(0, 0, 500, 900, fill="#000022", outline="")
        else:
            self.canvas.create_rectangle(0, 0, 500, 900, fill="#000022", outline="")

        self.contact = contactpart(self.canvas)
        self.title_subtitle = title_subtitle_part(self.canvas)
        self.logo = logopart(self.canvas)
        self.login_button = loginpart(self.canvas)
        self.signup_button = signinpart(self.canvas)
        self.cag = cagpart(self.canvas)  # continue as guest
        self.help = helpinformationpart(self.canvas)
        self.information = imforamtionpart(self.canvas)


class contactpart():  
    def __init__(self, root):
        self.cpf = Frame(root, bg="#5588ff")
        self.cpf.place(x=40, y=10, width=30, height=30)
        self.cpl = Label(self.cpf, bg="#5588ff")
        self.cpl.place(relwidth=1, relheight=1)

        self.cef = Frame(root, bg="#55cc99")
        self.cef.place(x=90, y=10, width=30, height=30)
        self.cel = Label(self.cef, bg="#55cc99")
        self.cel.place(relwidth=1, relheight=1)

        self.cwf = Frame(root, bg="#ff88aa")
        self.cwf.place(x=140, y=10, width=30, height=30)
        self.cwl = Label(self.cwf, bg="#ff88aa")
        self.cwl.place(relwidth=1, relheight=1)


class title_subtitle_part():
    def __init__(self, root):
        self.tf = Frame(root, bg="black")
        self.tf.place(x=100, y=120, width=300, height=80)
        self.tl = Label(self.tf, text="SPACE VISION", fg="white", bg="black")
        self.tl.place(relwidth=1, relheight=1)

        self.stf = Frame(root, bg="black")
        self.stf.place(x=100, y=200, width=300, height=40)
        self.stl = Label(self.stf, text="See Beyond the Stars", fg="white", bg="black")
        self.stl.place(relwidth=1, relheight=1)


class logopart(): 
    def __init__(self, root):
        self.lpf = Frame(root)
        self.lpf.place(x=155, y=268, width=185, height=185)
        self.lpl = Label(self.lpf)
        self.lpl.place(relwidth=1, relheight=1)

        logo_candidates = [
            "/Users/weiqixuan/Desktop/ddt_work/SPACEVISION_T/assests/logo.png",
            "/Users/weiqixuan/Desktop/ddt_work/SPACEVISION_T/assets/logo.png",
        ]
        logo_path = next((p for p in logo_candidates if os.path.exists(p)), None)

        if logo_path:
            try:
                logo_img = Image.open(logo_path).resize((185, 185))
                self.logo_photo = ImageTk.PhotoImage(logo_img)
                self.lpl.config(image=self.logo_photo)
                self.lpl.image = self.logo_photo
            except Exception:
                self.lpl.config(text="LOGO", bg="gray", fg="white")
        else:
            self.lpl.config(text="LOGO", bg="gray", fg="white")


class loginpart():
    def __init__(self, root):
        self.lbf = Frame(root)
        self.lbf.place(x=150, y=460, width=200, height=40)
        self.lbl = Label(self.lbf, text="Login", bg="#0078D7", fg="white")
        self.lbl.place(relwidth=1, relheight=1)


class signinpart():
    def __init__(self, root):
        self.sbf = Frame(root)
        self.sbf.place(x=150, y=520, width=200, height=40)
        self.sbl = Label(self.sbf, text="Sign Up", bg="#00A36C", fg="white")
        self.sbl.place(relwidth=1, relheight=1)


class cagpart():
    def __init__(self, root):
        self.cagf = Frame(root)
        self.cagf.place(x=150, y=580, width=200, height=40)
        self.cagl = Label(self.cagf, text="Continue as Guest", bg="#444", fg="white")
        self.cagl.place(relwidth=1, relheight=1)


class helpinformationpart():
    def __init__(self, root):
        self.hif = Frame(root)
        self.hif.place(x=80, y=660, width=350, height=15)
        self.hil = Label(self.hif, text="Need Help? Contact us.", bg="black", fg="white")
        self.hil.place(relwidth=1, relheight=1)


class imforamtionpart(): 
    def __init__(self, root):
        self.imf = Frame(root)
        self.imf.place(x=350, y=740, width=130, height=10)
        self.ill = Label(self.imf, text="Version 1.0", bg="black", fg="white")
        self.ill.place(relwidth=1, relheight=1)


if __name__ == "__main__":
    program = Tk()
    app = skyguideapp(program)
    program.mainloop()
