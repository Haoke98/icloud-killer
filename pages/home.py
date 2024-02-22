# _*_ codign:utf8 _*_
"""====================================
@Author:Sadam·Sadik
@Email：1903249375@qq.com
@Date：2024/1/28
@Software: PyCharm
@disc:
======================================="""
import tkinter as tk
from tkinter import ttk


class HomePage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # 在主页上显示用户信息和头像
        self.welcome_label = tk.Label(self, text="")
        self.welcome_label.pack()

        # 创建头像图标
        # 这里使用一个简单的示例图片代替真实的用户头像
        photo = tk.PhotoImage(file="/Users/shadikesadamu/Documents/壁纸/20231106213414735.png").subsample(4, 4)
        avatar_label = tk.Label(self, image=photo)
        avatar_label.photo = photo
        avatar_label.pack()

        # 创建登录按钮
        self.login_button = tk.Button(self, text="开始同步", command=self.sync)
        self.login_button.pack()

        # 创建一个进度条
        self.progress_bar = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.progress_message = tk.Label(self)
        self.progress_message.pack()

        # 创建下拉菜单
        # menu_bar = tk.Menu(self)
        # self.config(menu=menu_bar)

        # 用户菜单
        # user_menu = tk.Menu(menu_bar, tearoff=0)
        # menu_bar.add_cascade(label=username, menu=user_menu)
        # user_menu.add_command(label="个人信息")
        # user_menu.add_separator()
        # user_menu.add_command(label="注销", command=lambda: self.logout())

    def show(self, username):
        self.welcome_label.config(text=f"欢迎回来，{username}！")
        self.pack()

    def sync(self):
        """
            同步数据
            :return:
            """
        iService = self.master.iService
        # for i, album_name in enumerate(iService.photos.albums):
        #     album = iService.photos.albums[album_name]
        #     print(i, album_name, len(album))
        all_photos = iService.photos.all
        total = len(all_photos)
        print(total)
        self.progress_bar["maximum"] = total
        for i, p in enumerate(all_photos):
            progress = (i + 1) / total * 100
            print(f"{progress:.2f}%({i + 1}/{total})", p, type(p), vars(p))
            # , p.id, p.filename, p.size, p.dimensions,
            #                   p.created,
            #                   p.asset_date,
            #                   p.added_date, p.versions
            self.progress_message.config(text=f"正在进行资源同步{progress:.2f}% ( {i + 1} / {total} )")
            self.progress_bar["value"] = i + 1
            self.update_idletasks()  # 更新Tkinter窗口
            if p.created != p.asset_date:
                raise Exception("异常数据")
            pass
        pass