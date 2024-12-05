# Import library yang akan digunakan
from tkinter import *
from tkinter.scrolledtext import *
from tkinter import messagebox
from datetime import datetime
import random, webbrowser

# Main class untuk GUI aplikasi chatbot
class MainWindow():
    # Inisiasi atribut utama untuk window
    def __init__(self, master):
        self.master = master
        # Mengatur judul dan ukuran window utama
        master.title("Chatbot Sederhana")
        master.geometry("480x430")
        # Parameter
        self.run = False
        self.mode = "Default"
        self.entry = False
        self.light = True

        '''Menu'''
        menubar = Menu(master) # Menambahkan menu bar ke aplikasi
        # Menu file untuk menyimpan, mereset sesi, atau keluar
        self.file_menu = Menu(menubar, tearoff=0, bg="#D6E6F2")
        self.file_menu.add_command(label="Simpan Sesi", command=self.save_chat)
        self.file_menu.add_command(label="Reset Sesi", command=self.reset_chat)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Keluar", command=master.destroy)
        # Menu untuk mengganti tema
        self.tema_menu = Menu(menubar, tearoff=0, bg="#D6E6F2")
        self.tema_menu.add_command(label="Ubah Tema", command=self.theme)
        # Menu tentang aplikasi
        self.tentang_menu = Menu(menubar, tearoff=0, bg="#D6E6F2")
        self.tentang_menu.add_command(label="Tentang Aplikasi", command=self.about)
        # Menambahkan menu ke menubar
        menubar.add_cascade(label="File", menu=self.file_menu)
        menubar.add_cascade(label="Tema", menu=self.tema_menu)
        menubar.add_cascade(label="Tentang", menu=self.tentang_menu)
        master.config(menu=menubar)

        '''Chat room'''
        self.txt = ScrolledText(master, width=55, height=20)
        self.txt.insert(END, "Chatbot: Halo! Ada yang bisa saya bantu?\n")
        self.txt.config(state=DISABLED)
        self.txt.pack(padx=10, pady=10, fill=BOTH, expand=True)

        '''Buttons'''
        # Frame untuk buttons
        self.button_frame = Frame(master)
        self.button_frame.pack(padx=10, pady=5, fill=X)
        # Menambahkan button ke frame
        self.spacer1_frame = Frame(self.button_frame)
        self.spacer1_frame.pack(side=LEFT, expand=True, fill=X)
        self.jokes_button = Button(self.button_frame, text="Buat Lelucon", command=self.buat_lelucon)
        self.jokes_button.pack(side=LEFT, padx=5)
        self.time_button = Button(self.button_frame, text="Tanya Jam", command=self.tanya_jam)
        self.time_button.pack(side=LEFT, padx=5)
        self.math_button = Button(self.button_frame, text="Soal Matematika", command=self.soal_matematika)
        self.math_button.pack(side=LEFT, padx=5)
        self.youtube_button = Button(self.button_frame, text="YouTube", command=self.youtube,)
        self.youtube_button.pack(side=LEFT, padx=5)
        self.spacer2_frame = Frame(self.button_frame)
        self.spacer2_frame.pack(side=LEFT, expand=True, fill=X)

        '''User entry/input field'''
        # Frame untuk entry field dan "Kirim" button
        self.entry_frame = Frame(master)
        self.entry_frame.pack(padx=10, pady=5, fill=X)
        # Entry field untuk user input
        self.chat = StringVar()
        self.field_chat = Entry(self.entry_frame, textvariable=self.chat)
        self.field_chat.pack(side=LEFT, fill=X, expand=True, padx=5)
        # Button untuk mengirim pesan
        self.send_button = Button(self.entry_frame, text="Kirim", command=self.response_chat)
        self.send_button.pack(side=RIGHT, padx=5)

    def time_now(self): # Fungsi untuk mendaptkan real time
        time = datetime.now()
        return time.strftime("%Y-%m-%d_%H-%M-%S") # Formatting tahun-bukan-hari_jam-menit-detik
    
    def save_chat(self): # Fungsi untuk menyimpan sesi chat ke file txt
        if self.run == True: # Check apakah sudah ada interaksi antara user dan bot
            chat_session = open(f"chat_session_{self.time_now()}.txt", "w", encoding="utf-8") # Membuat file baru
            chat_session.write(self.txt.get("1.0", END).strip()) # Mengambil isi self.txt dari baris 1 sampai terakhir
            chat_session.close() # Menutup file
            messagebox.showinfo("Sukses", message=f"Sesi percakapan berhasil disimpan sebagai 'chat_session_{self.time_now()}.txt'.")
        else:
            messagebox.showinfo("Info", message="Tidak ada sesi untuk disimpan.") # Menampilkan popup info
    
    def reset_chat(self): # Fungsi untuk mereset chat
        self.run = False # Update parameter run
        self.mode = "Default" # Update parameter mode
        self.txt.config(state=NORMAL) # Mengubah state ke normal agar bisa ditulis
        self.txt.delete("1.0", END) # Delete seluruh isi dari self.txt
        self.txt.insert(END, "Chatbot: Halo! Ada yang bisa saya bantu?\n") # Menambahkan kembali pesan awal bot
        self.txt.config(state=DISABLED) # Mengubah kembali agar self.txt tidak bisa diubah-ubah
        messagebox.showinfo("Reset", message="Sesi telah direset.")
    
    def theme(self): # Fungsi untuk mengubah tema
        if self.light: # Jika tema sekarang light/default
            self.master.config(bg="#333333") # Mengubah warna
            for menu in (self.file_menu, self.tema_menu, self.tentang_menu): # Ubah bg dan fg menu
                menu.config(bg="#264369", fg="white")
            for frame in (self.button_frame, self.spacer1_frame, self.spacer2_frame, self.entry_frame): # Ubah bg frame
                frame["bg"] = "#333333"
            for button in (self.jokes_button, self.time_button, self.math_button, self.youtube_button, self.send_button): # Ubah bg dan fg button
                button.config(bg="grey", fg="black")
            self.field_chat.config(bg="black", fg="white", insertbackground="white")
            self.txt.config(bg="black", fg="white", highlightbackground="lightgrey") # Ubah untuk scrolledtext nya
            self.light = False # Update parameter light
        else: # Jika tema sekarang hitam, kembalikan ke light
            self.master.config(bg="#F0F0F0")
            for menu in (self.file_menu, self.tema_menu, self.tentang_menu):
                menu.config(bg="#D6E6F2", fg="black")
            for frame in (self.button_frame, self.spacer1_frame, self.spacer2_frame, self.entry_frame):
                frame["bg"] = "#F0F0F0"
            for button in (self.jokes_button, self.time_button, self.math_button, self.youtube_button, self.send_button):
                button.config(bg="#F0F0F0", fg="black")    
            self.field_chat["bg"] = "white"
            self.field_chat.config(bg="white", fg="black", insertbackground="black")
            self.txt.config(bg="white", fg="black", highlightbackground="lightgrey")
            self.light = True
    
    def about(self): # Fungsi untuk menampilkan pesan tentang aplikasi
        messagebox.showinfo("Tentang Aplikasi", 
                            message="Aplikasi Chatbot ini dikembangkan oleh Keisha Vania Laurent dari FASILKOM UI di tahun 2024.\n"
                                    "Semoga aplikasi ini dapat menjadi pembelajaran yang bermanfaat, have a great day!")

    def buat_lelucon(self): # Fungsi untuk menampilkan lelucon
        self.run = True # Update parameter run
        self.mode = "Joke" # Update parameter mode
        self.txt.config(state=NORMAL)
        self.txt.insert(END, "User: Buat lelucon\n") if not self.entry else None # Jika user akses dari tombol maka akan menampilkan "buat lelucon"
        self.txt.insert(END, f"Chatbot: {random.choice(jokes)}\n") # Mengambil jokes random dari kumpulan jokes yang sudah dibuat
        self.txt.config(state=DISABLED)
        self.txt.see(END) # Secara otomatis scroll mengikuti text terakhir kali
    
    def tanya_jam(self): # Fungsi untuk menampilkan waktu
        self.run = True
        self.mode = "Info"
        self.txt.config(state=NORMAL)
        self.txt.insert(END, "User: Tanya jam\n") if not self.entry else None
        # Memanggil fungsi time_now untuk mendapatkan real time tapi di slicing karena cuma mau diambil bagian jam-menit-waktu, dan mengubah "-" jadi ":"
        self.txt.insert(END, f"Chatbot: Saat ini pukul {self.time_now()[11:].replace("-", ":")}.\n")
        self.txt.config(state=DISABLED)
        self.txt.see(END)
    
    def soal_matematika(self): # Fungsi untuk menampilkan soal matematika
        # Random angka dari 0-9
        self.a = random.randint(0, 9)
        self.b = random.randint(0, 9)
        self.run = True
        self.mode = "Math"
        self.txt.config(state=NORMAL)
        self.txt.insert(END, "User: Beri aku soal matematika\n") if not self.entry else None
        self.txt.insert(END, f"Chatbot: Berapa {self.a} + {self.b}?\n") # Menampilkan soal a + b
        self.txt.config(state=DISABLED)
        self.txt.see(END)
    
    def youtube(self): # Fungsi untuk menampilkan/membuka video youtube
        self.run = True
        self.mode = "Youtube"
        self.txt.config(state=NORMAL)
        self.txt.insert(END, "User: Nonton YouTube\n") if not self.entry else None
        self.txt.insert(END, f"Chatbot: Video seperti apa yang ingin anda tonton?\n") # Tanya kepada user
        self.txt.config(state=DISABLED)
        self.txt.see(END)

    def response_chat(self): # Fungsi untuk respon chat dari user
        self.run = True
        user_input = self.chat.get().strip() # Mengambil nilai self.chat dan distrip untuk menghilangkan whitespace di ujung string
        if not user_input: # Kalau input user kosong
            return None
        self.txt.config(state=NORMAL)
        self.txt.insert(END, f"User: {user_input}\n") # Menampilkan input dari user
        self.found = False
        
        def trigger_response(): # Fungsi untuk input yang men-trigger tombol-tombol seperti lelucon, jam, soal matematika, dan youtube
            for idx, tpl in enumerate(button_responses): # Check apakah input sesuai dengan keyword di button_responses
                for response in tpl:
                    if not self.found and response in user_input.lower():
                        self.found = True # Update parameter
                        self.entry = True
                        [self.buat_lelucon, self.tanya_jam, self.soal_matematika, self.youtube][idx]() # Memanggil fungsi sesuai idx
                        self.entry = False
                        break
            if not self.found and self.mode != "Default": # Kalau belum ketemu, check di default_responses
                for key in default_responses:
                    for response in key:
                        if not self.found and response in user_input.lower():
                            self.txt.insert(END, f"Chatbot: {random.choice(default_responses[key])}\n") # Memanggil random dari value key nya
                            self.found = True
                            self.mode = "Default"
                            break
        
        def handle_response(response_dict, mode_reset=True): # Fungsi utama untuk menghandle respon
            if not self.found and self.mode in ("Default", "Joke", "Info"): # Check dulu apakah input merupakan trigger untuk tombol
                trigger_response()
            for key, responses in response_dict.items(): # Check apakah input ada di response_dict
                for response in key:
                    if not self.found and response in user_input.lower():
                        if self.mode == "Math": # Jika mode math
                            self.txt.insert(END, f"Chatbot: {random.choice(responses)}. Jawaban yang benar adalah {self.a+self.b}.\n")
                        else: # Jika mode lain
                            self.txt.insert(END, f"Chatbot: {random.choice(responses)}\n")
                        self.found = True
                        if mode_reset:
                            self.mode = "Default"
                        break

        if self.mode == "Default":
            handle_response(default_responses)

        elif self.mode == "Joke":
            handle_response(joke_responses)

        elif self.mode == "Info":
            handle_response(info_responses)

        elif self.mode == "Math":
            contains_num = [char for char in user_input if char.isdigit()] # Mengambil angka yang ada di input
            if contains_num: # Jika list tidak kosong
                user_numbers = ''.join(contains_num) # Menggabungkan list angka shg terbentuk sebuah bilangan
                if self.a + self.b == int(user_numbers): # Kalau a + b = jawaban user (angka yg udah digabung) -> jawaban benar
                    self.txt.insert(END, f"Chatbot: {random.choice(math_responses['benar'])}\n")
                else: # Jawaban salah
                    self.txt.insert(END, f"Chatbot: {random.choice(math_responses['salah'])}. Jawaban yang benar adalah {self.a + self.b}.\n")
                self.found = True
                self.mode = "Default"
            else: # Jika user tidak memasukan angka, check apakah input ada di math_responses["respon"] dgn memanggil fungsi handle_response
                handle_response(math_responses["respon"])

        elif self.mode == "Youtube":
            def play_video(choice): # Fungsi untuk play video
                formatted_choice = choice.split("*") # Memisahkan choice berdasarkan "*"
                if "Selamat!" not in formatted_choice[0]: # Menampilkan pesan dari chatbot
                    self.txt.insert(END, f'Chatbot: Memainkan "{formatted_choice[0]}".\n')
                else:
                    self.txt.insert(END, f"Chatbot: {formatted_choice[0]}.\n")
                webbrowser.open(formatted_choice[1]) # Membuka link di browser default

            for key, videos in yt_responses.items(): # Check input di yt_responses
                for response in key:
                    if not self.found and response in user_input.lower():
                        play_video(random.choice(videos)) # Memanggil fungsi play_video dgn choice generate random dari value dict
                        self.found = True
                        self.mode = "Default"
                        break
            for word in ("bebas", "apa aja", "serah"): # Kalau di atas belum ketemu, check lagi input user
                if not self.found and word in user_input.lower():
                    play_video(random.choice(yt_responses[random.choice(tuple(yt_responses.keys()))])) # Memanggil fungsi play_video dgn choice generate random dari key dan juga valuenya
                    self.found = True
                    self.mode = "Default"

        if not self.found: # Kalau pada akhirnya tetap nggak ketemu
            fallback_messages = {"Default": "Maaf saya tidak mengerti.",
                                 "Joke": "Maaf saya tidak mengerti.",
                                 "Info": "Maaf saya tidak mengerti.",
                                 "Math": "Masukkan angka yang valid sebagai jawaban.",
                                 "Youtube": "Maaf, video yang anda minta belum tersedia."}
            self.txt.insert(END, f"Chatbot: {fallback_messages[self.mode]}\n") # Respon bot sesuai mode
            self.mode = "Default"

        self.field_chat.delete(0, END) # Hapus kolom untuk mengetik
        self.txt.config(state=DISABLED) # Ubah state ke disabled agar scrolledtext tidak bisa diubah-ubah
        self.txt.see(END) # Secara otomatis scroll mengikuti text terakhir kali
        
'''Kamus untuk me-respons user'''
default_responses = {("hai", "halo", "hello"): ("Halo!", "Hai juga!", "HALOOOOOOOO!", "Hai, senang bertemu denganmu ^___^"),
                    ("apa kabar", "how's life", "piye kabare"): ("Saya baik, terima kasih!", "Saya baik, semoga harimu juga baik!", "Semua baik di sini!", "Saya baik tentunya!", "Saya capek jadi bot :c"),
                    ("terima kasih", "makasih", "thank you", "thanks", "suwun"): ("Sama-sama!", "Tidak masalah!", "Senang bisa membantu!", "You are welcome!", "Glad to help!", "No problem!", "Sami-sami"),
                    ("selamat tinggal", "goodbye", "bye", "dadah"): ("Sampai jumpa!", "Semoga kita bertemu lagi!", "Semoga harimu menyenangkan!", "Dadah!", "Bye!", "Good bye!"),
                    ("senang", "bahagia", "happy"): ("Aku ikut senang mendengarnya!", "Hebat! Tetap semangat ya!", "Wah, itu kabar baik!"),
                    ("sedih", "nangis"): ("Jangan bersedih, semuanya akan baik-baik saja.", "Kadang hidup memang sulit, tapi kamu pasti bisa melewati ini."),
                    ("marah", "kesal"): ("Cobalah tarik napas dalam-dalam, itu bisa membantu.", "Aku paham perasaanmu. Semoga cepat tenang.", "Jangan biarkan amarah menguasaimu."),
                    ("capek", "tired"): ("Istirahatlah sejenak, kamu pasti lelah.", "Minum air dan relaks sebentar, ya.", "Capek itu wajar, jangan lupa beri waktu untuk dirimu sendiri."),
                    ("wow", "keren", "mantap"): ("Terima kasih atas pujiannya!", "Wow! Saya tahu saya keren /dab", "Haha bisa saja :3", "Thank you! Saya masih harus berkembang."),
                    ("haha", "awok", "wk"): ("Hahaha saya ikut ketawa nih.", "AWOKAOWKAOKWOKKAOWK.", "Hahaha, lucu banget."),
                    ("ok",): ("Oke! Apa ada hal lain yang bisa dibantu?", "Baik! Saya siap membantu anda.")}

button_responses = (("lelucon", "joke"), ("info", "jam", "waktu", "sekarang"), ("soal", "matematika", "itung"), ("video", "youtube", "nonton"))

joke_responses = {("ga", "garing", "aneh"): ("Maaf jika lelucon yang saya berikan tidak lucu.", "Yah, selera humor kita berbeda nih :c", "Selera humor saya terlalu rendah, ya?", "Maaf, saya terlalu receh untuk anda."),
                  ("lumayan", "begitu ya"): ("Semoga lelucon ini dapat mewarnai harimu!", "Jangan lupa senyum ya!", "Haha, ketawa dong!")}

info_responses = {("baik", "ok", "ya"): ("Jangan lupa istirahat sejenak, ya! Waktu terus berjalan.", "Waktu menunjukkan jam sekarang, tetapi jangan khawatir, saya tidak akan mengejar waktu!", 
                                                                                              "Waktu adalah hal yang penting. Semoga hari ini berjalan dengan lancar!", "Sama-sama! Semoga harimu menyenangkan :D"),
                  ("cuaca", "panas", "hujan"): ("Saya tidak bisa memeriksa cuaca secara real time, tapi semoga cuacanya cerah di sana!", "Pastikan untuk membawa payung jika cuaca mendung!", "Cek cuaca di smartphone kamu ya, supaya tidak ketinggalan informasi.",
                                                "Cuaca mungkin berbeda di tempatmu, tapi semoga selalu menyenangkan!", "Lah, kok tanya saya.")}

math_responses = {"benar": ("Jawaban anda benar!", "Wah, anda pintar sekali!", "Seratus untuk anda!", "Jawaban anda salah, tapi bohong."),
                  "salah": ("Jawaban anda salah", "Yah, kurang tepat nih", "Waduh, bukan segitu hasilnya", "Salah"),
                  "respon": {("ga", "nyerah"): ("Baik jika anda menyerah", "Yah, masa gitu aja nyerah?"),
                             ("pusing", "bingung", "susah"): ("Jangan dibawa pusing", "Yah, baiklah jika anda kebingungan")}}

yt_responses = {("lagu", "song", "musi", "mv", "nyanyi"): ("Something About You - Eyedress & Dent May*https://youtu.be/j9yEL3B5Cvk?si=h60-2xwDm-Wjhk0m", 
                                                           "Infrunami - Steve Lacy*https://youtu.be/Ol0-9Ob-QNk?si=nhMYYjusAovmpiAM", 
                                                           "Dark Red - Steve Lacy*https://youtu.be/xRzbLQ_WKPs?si=FqbbzOlRLD4v1pXS",
                                                           "How Can You Be Sure? - Radiohead*https://youtu.be/IOax8WSeEGM?si=pXBP2QCRNaBTuD8p",
                                                           "My Iron Lung - Radiohead*https://youtu.be/pRU-6vaKaf4?si=WpVSS3Ndolh6Ki8V",
                                                           "Jigsaw Falling Into Place - Radiohead*https://youtu.be/GoLJJRIWCLU?si=kkNreeWN98t-m70N",
                                                           "Black Star - Radiohead*https://youtu.be/d7lbzUUXj0k?si=kdTSsipXpX1Uui8r",
                                                           "Married With Children - Oasis*https://youtu.be/o-cMaASaU4Q?si=RoEjF15exM1Qcyxj",
                                                           "Snow (Hey Oh) - Red Hot Chili Peppers*https://youtu.be/yuFI5KSPAt4?si=_suZOLeZcK71lJmG",
                                                           "Lovers Rock - TV Girl*https://youtu.be/j_sG_Juncn8?si=9p89XawDgWQvVVJw",
                                                           "Kiss Me - Sixpence None The Richer*https://youtu.be/K2tbQ_g2VbQ?si=9ajrGxWtLiZNcMSb",
                                                           "Linger - The Cranberries*https://youtu.be/G6Kspj3OO0s?si=bzIChHr1FKa2wNJA",
                                                           "Chamber Of Reflection - Mac DeMarco*https://youtu.be/pQsF3pzOc54?si=GDqkzC0xoeV29jo-"
                                                           "Selamat! Anda terkena Rick Rolled*https://youtu.be/dQw4w9WgXcQ?si=Oj3fbM3nxZ_YhXJZ"),
                ("game", "permainan", "stream"): ("Film Yang Jadi Game Horror - A Quiet Place Indonesia*https://youtu.be/QYjh5iekQVE?si=3CuGIOti4dO5wkXN",
                                                  "Game Horror Yang Sedih - Bad Parenting Indonesia*https://youtu.be/338st42F3eE?si=7jSoejtnyh0g1rbb",
                                                  "Kembalinya Sang Bapake - Secret Neighbor Indonesia*https://youtu.be/zhXz39-7CRc?si=AnLnXT4Lbt46Jul3",
                                                  "Ini Sih Kek Real Banget - Backrooms: Escape Together Indonesia*https://youtu.be/L1cVpWyrEGA?si=vysjmJVkFM8Oy_03",
                                                  "SEDIKIT LAGI PERJALANAN SAMPAI! TAPI KOK.... Euro Truck Simulator 2 GAMEPLAY #4*https://www.youtube.com/live/J6nKBfdR5IA?si=iZI86zmaqlKWtL5x",
                                                  "GAME ADAPTASI KISAH NYATA HOROR PALING MENGERIKAN DI TAIWAN AKHIRNYA RILIS.... Incantation*https://www.youtube.com/live/hEJ5KT1Kwqs?si=y50Q7ecV06FbwHI8",
                                                  "ADA MISTERI MENGERIKAN DI RUMAH JEPANG INI! Jisatsu | 自撮*https://www.youtube.com/live/GhkqYwMGM_s?si=F_ABqlIfZ6PVHWey",
                                                  "Judul Gamenya Adalah IBLIS*https://www.youtube.com/live/atC56l_qYxs?si=Io8vDB5wK-emXfPF",
                                                  "PETUALANGAN KUCING DIMULAI! Stray GAMEPLAY#1*https://www.youtube.com/live/7phNNrctGRM?si=F4V-fke7Zfj0k2SB"),
                ("edukasi", "pengetahuan"): ("MENGAPA WAKTU BEGITU MERAHASIAKAN DIRINYA?*https://youtu.be/OwxJ44qti2s?si=xA3f0oBGbmo6x5kP",
                                             "200.000+ Tahun Perjalanan Manusia, dalam 13 Menit*https://youtu.be/Nu16eO1Qu88?si=kF4S-QSFpQ_4bCu7", 
                                             "Apakah Ada yang Lebih Kecil dari Atom?*https://youtu.be/AxyPASIXz1k?si=HZrJXQqHqxQ-jlXZ",
                                             "Animation vs. Math*https://youtu.be/B1J6Ou4q8vE?si=cWUQt_UOaeXp0jUX",
                                             "Discovery That Changed Physics! Gravity is NOT a Force!*https://youtu.be/3pZNzF6LBII?si=zU08jtolyyc7ObCy",
                                             "The Origin of Consciousness - How Unaware Things Became Aware*https://youtu.be/H6u0VBqNBQ8?si=MqFpJ7pNd5zAjhUU",
                                             "The Paradox of an Infinite Universe*https://youtu.be/isdLel273rQ?si=1Qv7ZalKO6cUO0t5"),
                ("asmr", "cook", "food", "masak", "makan"): ("The Best BEEF STEW with Baked Bread in the Forest | Relaxing Cooking with ASMR*https://youtu.be/4jm-1EcLWM4?si=xD4KUpo6bi8jbioZ",
                                                             "Juicy Steak Cooked on a Campfire | Wild Cuisine ASMR in the Forest*https://youtu.be/m3HiLrFzZ5w?si=YH3nplnYW_lgI1Hc",
                                                             "🔥Whole Chicken Prepared in the Forest🔥 Relaxing Cooking*https://youtu.be/Ak34skdOeNI?si=Vld-MT2qm4vR205E",
                                                             "Making Dinner in 1796 |Fire Cooking Delicious Meat| ASMR Real Historic Recipes*https://youtu.be/QALo9woiXLU?si=3XAcTt2lyW85wkXf",
                                                             "A Rainy Day's Cooking in 1828 |200 Year Old Recipes| Historical ASMR Cooking*https://youtu.be/cKdG-VJAMDI?si=ozGEkTSlQ7V5W93a",
                                                             "Tokyo's most ASMR Chef preparing Hida Wagyu & Lobster*https://youtu.be/ynlodR5dw-0?si=5oMkzHkNRU3VCoo6",
                                                             "The Most Famous Ramen Vending Machine Restaurant*https://youtu.be/AFeKB9YDy-g?si=osCSUN7J_Xi5otXb",
                                                             "$53 High-end Fried Rice - Wok Skills of Master Chef in Hong Kong*https://youtu.be/u9nry4Psey4?si=xF8_1SZ2vo7ew9Nz",
                                                             "Market show: Yummy river shrimp, crispy pork and fry rice cooking - Countryside Life TV*https://youtu.be/tfLBQGh93J4?si=Ej0H4t5r_bSlzAzJ")}

jokes = ("Makanan makanan apa yang gampang dibuat? Tahu easy hahaha.",
         "Kenapa air laut rasanya asin? Karena kena keringet ikan.",
         "Kenapa bola basket tidak boleh basah? Karena harus dilempar ke ring.",
         "Kalau anda diselimuti masalah berarti anda manusia, kalau anda diselimuti wijen berarti anda onde-onde.",
         "Kenapa ginjal ada dua? Karena kalau satu ganjil, kalau tiga Ganjar.",
         "Buah apa yang bisa ketawa? Buah pis ang ang ang",
         "Ke apotik beli obat tidur, pas pulang bawanya pelan-pelan. Tau tidak kenapa? Soalnya takut obatnya bangun.",
         "Anda tau cembilan tidak? Cemilan itu cecudah delapan cebelum cepuluh.",
         "Abis minum marjan terus kejang-kejang, ternyata saya kesirupan.",
         "Sehabis pulang, masuk kamar, saya kaget kok kasurnya tidak ada, oh ternyata ketutupan sprei.",
         "Maaf tidak bisa jokes, soalnya jokesnya ada di motor.",
         "Kenapa ya kipas angin di rumah saya aneh? Dari tadi nengok kanan kiri tapi kok ngga nyebrang-nyebrang.")

if __name__ == "__main__":
    root = Tk() # Membuat jendela utama aplikasi
    main = MainWindow(root) # Mendefinisikan dan mengatur elemen GUI pada jendela tersebut
    root.mainloop() # Agar tetap berjalan dan merespons event user