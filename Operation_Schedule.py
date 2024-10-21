from tabulate import tabulate
from datetime import datetime

operation = [
    {'Kode Operasi': 'OP-111', 'Id Dokter': 1289, 'Nama Dokter': 'Yusuf Idris', 'Nama Pasien': 'Ahmad Panca', 'Tanggal Operasi': datetime(2024, 11, 1).date(), 'Ruang Operasi': 1, 'Nama Operasi': 'Bypass'},
    {'Kode Operasi': 'OP-123', 'Id Dokter': 3872, 'Nama Dokter': 'Dion Hasan', 'Nama Pasien': 'Malika Handayani', 'Tanggal Operasi': datetime(2024, 11, 2).date(), 'Ruang Operasi': 2, 'Nama Operasi': 'Appendektomi'},
    {'Kode Operasi': 'OP-378', 'Id Dokter': 7302, 'Nama Dokter': 'Melisa Utari', 'Nama Pasien': 'Salma Merian', 'Tanggal Operasi': datetime(2024, 11, 2).date(), 'Ruang Operasi': 3, 'Nama Operasi': 'Craniotomy'},
    {'Kode Operasi': 'OP-981', 'Id Dokter': 3872, 'Nama Dokter': 'Dion Hasan', 'Nama Pasien': 'Sada Agung', 'Tanggal Operasi': datetime(2024, 11, 3).date(), 'Ruang Operasi': 2, 'Nama Operasi': 'Hernia'},
    {'Kode Operasi': 'OP-521', 'Id Dokter': 4379, 'Nama Dokter': 'Flora Agustina', 'Nama Pasien': 'Mita Amalia', 'Tanggal Operasi': datetime(2024, 11, 7).date(), 'Ruang Operasi': 5, 'Nama Operasi': 'Caesarean Section'},
    {'Kode Operasi': 'OP-692', 'Id Dokter': 5281, 'Nama Dokter': 'Belinda Prilia', 'Nama Pasien': 'Toni Wiyoko', 'Tanggal Operasi': datetime(2024, 11, 11).date(), 'Ruang Operasi': 1, 'Nama Operasi': 'Skoliosis'},
    {'Kode Operasi': 'OP-704', 'Id Dokter': 8349, 'Nama Dokter': 'Ratu Brizia', 'Nama Pasien': 'Melinda Putri', 'Tanggal Operasi': datetime(2024, 11, 4).date(), 'Ruang Operasi': 4, 'Nama Operasi': 'Angioplasti Koroner'},
    {'Kode Operasi': 'OP-489', 'Id Dokter': 9823, 'Nama Dokter': 'Lilo Miputra', 'Nama Pasien': 'Tian Rasyid', 'Tanggal Operasi': datetime(2024, 12, 1).date(), 'Ruang Operasi': 4, 'Nama Operasi': 'Artroskopi Lutut'},
    {'Kode Operasi': 'OP-903', 'Id Dokter': 1289, 'Nama Dokter': 'Yusuf Idris', 'Nama Pasien': 'Putra Raden', 'Tanggal Operasi': datetime(2024, 12, 5).date(), 'Ruang Operasi': 2, 'Nama Operasi': 'Implantasi Pacemaker'},
    {'Kode Operasi': 'OP-435', 'Id Dokter': 4379, 'Nama Dokter': 'Flora Agustina', 'Nama Pasien': 'Kirana Rustina', 'Tanggal Operasi': datetime(2024, 11, 4).date(), 'Ruang Operasi': 3, 'Nama Operasi': 'Histerektomi'}
]

doctor_data = {
    1289: {'Nama Dokter': 'Yusuf Idris', 'Departemen': 'Kardiologi', 'No. Telp': '082923892123'},
    2849: {'Nama Dokter': 'Dila Mawar', 'Departemen': 'Bedah Umum', 'No. Telp': '085673984831'},
    7302: {'Nama Dokter': 'Melisa Utari', 'Departemen': 'Bedah Saraf', 'No. Telp': '081928374659'},
    4379: {'Nama Dokter': 'Flora Agustina', 'Departemen': 'Obstetri dan Ginekologi', 'No. Telp': '081567123456'},
    3872: {'Nama Dokter': 'Dion Hasan', 'Departemen': 'Bedah Umum', 'No. Telp': '081291827364'},
    1234: {'Nama Dokter': 'Putri Kusuma', 'Departemen': 'Bedah Umum', 'No. Telp': '081112121212'},
    4345: {'Nama Dokter': 'Farida Putri', 'Departemen': 'Obstetri dan Ginekologi', 'No. Telp': '081238479911'},
    8349: {'Nama Dokter': 'Ratu Brizia', 'Departemen': 'Kardiologi', 'No. Telp': '081384757171'},
    9823: {'Nama Dokter': 'Lilo Miputra', 'Departemen': 'Orthopedi', 'No. Telp': '081154739125'},
    5281: {'Nama Dokter': 'Belinda Prilia', 'Departemen': 'Orthopedi', 'No. Telp': '085729481004'}
}



# ========== MAIN OPTION ========== #
def mainoption():
    while True:
        print("""
  ──────────────────────── ✙ ✙ ✙ ────────────────────────
                    SERENITY HOSPITAL
              OPERATION SCHEDULE - MAIN OPTION
  ───────────────────────────────────────────────────────
    1. Tampilkan Jadwal Operasi
    2. Tambah Jadwal Operasi
    3. Ubah Data Operasi
    4. Cancel Jadwal Operasi
    5. Exit Program
⚕️ ─────────────────────────────────────────────────────── ⚕️
              """)
        try:
            option = int(input('Masukkan opsi yang ingin dijalankan: '))
            if option == 1:
                show()
            elif option == 2:
                add()
            elif option == 3:
                edit()
            elif option == 4:
                cancel()
            elif option == 5:
                break
            else:
                print('Opsi yang Anda pilih tidak tersedia, silakan masukkan kembali.\n')
        except ValueError:
            print('Input tidak valid, mohon hanya masukkan angka.\n')



# ========== OPTION 1 ========== #
def show():
    while True:
        print("""
  ──────────────────────── ✙ ✙ ✙ ────────────────────────
                    SERENITY HOSPITAL
                       SHOW OPTION
  ───────────────────────────────────────────────────────
    1. Tampilkan Seluruh Jadwal Operasi
    2. Tampilkan Data Berdasarkan Kode Operasi
    3. Tampilkan Data Berdasarkan Kolom
    4. Tampilkan Data Terurut Berdasarkan Kolom
    0. Kembali ke Opsi Utama              
⚕️ ─────────────────────────────────────────────────────── ⚕️
              """)
        try:
            show_option = int(input('Masukkan opsi yang ingin dijalankan: '))
            if show_option == 1:
                show_all_sched()
            elif show_option == 2:
                show_by_pk()
            elif show_option == 3:
                print(f'Kolom yang dapat dipilih: {col_name[1:]}')
                while True:
                    col = input('\nMasukkan nama kolom: ').lower()
                    if col == 'id dokter':
                        show_by_doc()
                        break
                    elif col == 'nama dokter':
                        show_by_doc_name()
                        break
                    elif col == 'nama pasien':
                        show_by_pat_name()
                        break
                    elif col == 'tanggal operasi':
                        show_by_date()
                        break
                    elif col == 'ruang operasi':
                        show_by_room()
                        break
                    elif col == 'nama operasi':
                        show_by_op_name()
                        break
                    else:
                        print('Kolom tidak ada.')
            elif show_option == 4:
                print(f'Kolom yang dapat dipilih: {col_name}')
                while True:
                    col_name_sort = input('\nMasukkan nama kolom: ').lower()
                    if col_name_sort == 'kode operasi':
                        show_sorted_pk()
                        break
                    elif col_name_sort == 'id dokter':
                        show_sorted_doc_id()
                        break
                    elif col_name_sort == 'nama dokter':
                        show_sorted_doc_name()
                        break
                    elif col_name_sort == 'nama pasien':
                        show_sorted_pat()
                        break
                    elif col_name_sort == 'tanggal operasi':
                        show_sorted_date()
                        break
                    elif col_name_sort == 'ruang operasi':
                        show_sorted_room()
                        break
                    elif col_name_sort == 'nama operasi':
                        show_sorted_op_name()
                        break
                    else:
                        print('Kolom tidak ada.')
            elif show_option == 0:
                return
            else:
                print('Opsi yang Anda pilih tidak tersedia, silakan masukkan kembali.\n')
        except ValueError:
            print('Input tidak valid, mohon hanya masukkan angka.\n')

def show_all_sched():
    if operation != []:
        print("""
                                            ⚕️ ───── Jadwal Operasi ───── ⚕️
             """)
        print(tabulate(operation, headers='keys', tablefmt='mixed_outline', numalign='center'))
        return
    else:
        print('Tidak ada data operasi.\n')
        return

def show_by_pk():
    if operation != []:
        pk_data_table()
    else:
        print('Data operasi yang Anda cari tidak ada.\n')
        return

def show_by_doc():
    while True:
        doc_id_list = [k for k in doctor_data]
        print(f'\nId dokter yang dapat dipilih: {doc_id_list}')
        try:
            inp_doc = int(input('\nMasukkan id dokter yang ingin ditampilkan: '))
            if inp_doc in doc_id_list:
                doc_id_data = [data for data in operation if data['Id Dokter'] == inp_doc]
                if doc_id_data:
                    print("""
                                            ⚕️ ───── Jadwal Operasi ───── ⚕️
                        """)
                    print(tabulate(doc_id_data, headers='keys', tablefmt='mixed_outline', numalign='center'))
                    return
                else:
                    empty_table()
                    print(f'\nBelum ada jadwal operasi untuk dokter dengan id {inp_doc}.\n')
                    return
            else:
                print(f'Dokter dengan id {inp_doc} tidak ada.\n')
        except ValueError:
            print('Input tidak valid, mohon hanya masukkan angka.\n')

def show_by_doc_name():
    while True:
        doc_name_list = [i['Nama Dokter'] for i in doctor_data.values()]
        print(f'\nNama dokter yang dapat dipilih: {doc_name_list}')
        inp_doc_name = input('\nMasukkan nama dokter yang ingin ditampilkan: ').title()
        if inp_doc_name in doc_name_list:
            doc_name_data = [data for data in operation if data['Nama Dokter'] == inp_doc_name]
            if doc_name_data:
                print("""
                                            ⚕️ ───── Jadwal Operasi ───── ⚕️
                        """)
                print(tabulate(doc_name_data, headers='keys', tablefmt='mixed_outline', numalign='center'))
                return
            else:
                empty_table()
                print(f'\nBelum ada jadwal operasi untuk dokter {inp_doc_name}.\n')
                return
        else:
            print(f'Tidak ada dokter bernama {inp_doc_name}.\n')
            return

def show_by_date():
    while True:
        try:
            inp_date = input('\nMasukkan tanggal yang ingin ditampilkan (YYYY-MM-DD): ')
            inp_date_f = datetime.strptime(inp_date, '%Y-%m-%d').date()
        except ValueError:
            print('Input tidak valid, mohon masukkan sesuai format (YYYY-MM-DD).')
            continue
        date_data = [data for data in operation if data['Tanggal Operasi'] == inp_date_f]
        if date_data:
            print("""
                                            ⚕️ ───── Jadwal Operasi ───── ⚕️
                        """)
            print(tabulate(date_data, headers='keys', tablefmt='mixed_outline', numalign='center'))
            return
        else:
            empty_table()
            print(f'Tidak ada jadwal operasi di tanggal {inp_date_f}.\n')
            return

def show_by_room():
    while True:
        try:
            inp_room = int(input('\nMasukkan ruang operasi yang ingin ditampilkan (1-5): '))
            if inp_room in range(1,6):
                op_room_data = [data for data in operation if data['Ruang Operasi'] == inp_room]
                if op_room_data:
                    print("""
                                            ⚕️ ───── Jadwal Operasi ───── ⚕️
                        """)
                    print(tabulate(op_room_data, headers='keys', tablefmt='mixed_outline', numalign='center'))
                    return
                else:
                    empty_table()
                    print(f'\nBelum ada jadwal operasi untuk ruang operasi {inp_room}.\n')
                    return
            else:
                print(f'Ruang operasi {inp_room} tidak ada.\n')
                return
        except ValueError:
            print('Input tidak valid, mohon hanya masukkan angka.')

def show_by_op_name():
    while True:
        inp_op_name = input('\nMasukkan nama operasi yang ingin ditampilkan: ').title()
        op_name_list = [data for data in operation if data['Nama Operasi'] == inp_op_name]
        if op_name_list:
            print()
            print(tabulate(op_name_list, headers='keys', tablefmt='mixed_outline', numalign='center'))
            return
        else:
            empty_table()
            print(f'Tidak ada operasi {inp_op_name}.\n')
            return
        
def show_by_pat_name():
    while True:
        inp_pat_name = input('\nMasukkan nama pasien yang ingin ditampilkan: ').title()
        pat_name_list = [data for data in operation if data['Nama Pasien'] == inp_pat_name]
        if pat_name_list:
            print()
            print(tabulate(pat_name_list, headers='keys', tablefmt='mixed_outline', numalign='center'))
            return
        else:
            empty_table()
            print(f'Tidak ada pasien bernama {inp_pat_name}.\n')
            return

def show_sorted_pk():
    operation_sorted = sorted(operation, key=lambda operation:operation['Kode Operasi'])
    print(tabulate(operation_sorted, headers='keys', tablefmt='mixed_outline', numalign='center'))

def show_sorted_doc_id():
    operation_sorted = sorted(operation, key=lambda operation:operation['Id Dokter'])
    print(tabulate(operation_sorted, headers='keys', tablefmt='mixed_outline', numalign='center'))

def show_sorted_doc_name():
    operation_sorted = sorted(operation, key=lambda operation:operation['Nama Dokter'])
    print(tabulate(operation_sorted, headers='keys', tablefmt='mixed_outline', numalign='center'))

def show_sorted_pat():
    operation_sorted = sorted(operation, key=lambda operation:operation['Nama Pasien'])
    print(tabulate(operation_sorted, headers='keys', tablefmt='mixed_outline', numalign='center'))

def show_sorted_date():
    operation_sorted = sorted(operation, key=lambda operation:operation['Tanggal Operasi'])
    print(tabulate(operation_sorted, headers='keys', tablefmt='mixed_outline', numalign='center'))

def show_sorted_room():
    operation_sorted = sorted(operation, key=lambda operation:operation['Ruang Operasi'])
    print(tabulate(operation_sorted, headers='keys', tablefmt='mixed_outline', numalign='center'))

def show_sorted_op_name():
    operation_sorted = sorted(operation, key=lambda operation:operation['Nama Operasi'])
    print(tabulate(operation_sorted, headers='keys', tablefmt='mixed_outline', numalign='center'))





# ========== OPTION 2 ========== #
def add():
    while True:
        print("""
  ──────────────────────── ✙ ✙ ✙ ────────────────────────
                    SERENITY HOSPITAL
                       ADD OPTION
  ───────────────────────────────────────────────────────    
    1. Tambahkan Jadwal Operasi
    0. Kembali ke Opsi Utama
⚕️ ─────────────────────────────────────────────────────── ⚕️
              """)
        try:
            add_option = int(input('Masukkan opsi yang ingin dijalankan: '))
            if add_option == 1:
                add_data()
            elif add_option == 0:
                return
            else:
                print('Opsi yang Anda pilih tidak tersedia, silakan masukkan kembali.\n')
        except ValueError:
            print('Input tidak valid, mohon hanya masukkan angka.\n')

def add_data():
    while True:
        op_code = input('\nMasukkan kode operasi: ').upper()
        if op_code.startswith('OP-') and op_code[3:].isdigit():
            break
        else:
            print('Format tidak valid, silakan masukkan kembali.\nFormat: OP-<code>')
    for i in operation:
        if op_code in i['Kode Operasi']:
            print(f'Data dengan kode operasi {op_code} sudah ada.')
            return
    list_doc = [k for k in doctor_data]
    new_patient = input('Masukkan nama pasien: ').title()
    new_op_name = input('Masukkan nama operasi: ').title()
    while True:
        while True:
            doctor_table()
            try:
                new_doctor = int(input('Masukkan id dokter: '))
                if new_doctor in list_doc:
                    break
                else:
                    print('Id Dokter tidak ada.\n')
            except ValueError:
                print('Invalid input, mohon hanya masukkan angka.\n')
        while True:
            try:
                inp_op_date = input('Masukkan tanggal operasi (YYYY-MM-DD): ')
                new_op_date = datetime.strptime(inp_op_date, '%Y-%m-%d').date()
                break
            except ValueError:
                print('Format tidak valid, mohon masukkan sesuai format (YYYY-MM-DD).\n')
        doc_date = [[i['Id Dokter'], i['Tanggal Operasi']] for i in operation]
        if [new_doctor, new_op_date] not in doc_date:
            break
        else:
            print(f'Dokter tidak tersedia pada tanggal {new_op_date}.\n')
            return
    while True:
        while True:
            try:
                new_op_room = int(input('Masukkan ruang operasi (1-5): '))
                if new_op_room in range(1,6):
                    break
                else:
                    print('Ruang operasi tidak tersedia. Mohon pilih antara ruang 1 sampai ruang 5.\n')
            except ValueError:
                print('Input tidak valid, mohon hanya masukkan angka (1-5).\n')
        date_room = [[i['Tanggal Operasi'], i['Ruang Operasi']] for i in operation]
        if [new_op_date, new_op_room] not in date_room:
            break
        else:
            print(f'Ruang operasi {new_op_room} untuk tanggal {new_op_date} sudah terisi.\n')
    while True:
        save = input('\nApakah Anda ingin menyimpan data? (Ya/Tidak): ').lower()
        if save == 'ya':
            new_data = {'Kode Operasi': op_code, 'Id Dokter': new_doctor, 'Nama Dokter': doctor_data[new_doctor]['Nama Dokter'], 'Nama Pasien': new_patient, 'Tanggal Operasi': new_op_date, 'Ruang Operasi': new_op_room, 'Nama Operasi': new_op_name}
            operation.append(new_data)
            print('\nData berhasil tersimpan.')
            return
        elif save == 'tidak':
            return
        else:
            print('Mohon hanya masukkan Ya atau Tidak.\n')



# ========== OPTION 3 ========== #
def edit():
    while True:
        print("""
  ──────────────────────── ✙ ✙ ✙ ────────────────────────
                    SERENITY HOSPITAL
                       EDIT OPTION
  ───────────────────────────────────────────────────────
    1. Ubah Data Operasi
    0. Kembali ke Opsi Utama
⚕️ ─────────────────────────────────────────────────────── ⚕️
              """)
        try:
            edit_option = int(input('Masukkan opsi yang ingin dijalankan: '))
            if edit_option == 1:
                pk_found = pk_data_table()
                if not pk_found:
                    continue
                exit = False
                while not exit:
                    edit = input('Apakah Anda ingin melanjutkan ubah data? (Ya/Tidak): ').lower()
                    if edit == 'ya':
                        while True:
                            col_edit = input('Masukkan kolom yang ingin Anda ubah: ').lower()
                            if col_edit == 'id dokter':
                                edit_by_doc_id()
                                exit = True
                                break
                            elif col_edit == 'tanggal operasi':
                                edit_by_date()
                                exit = True
                                break
                            elif col_edit == 'nama dokter':
                                edit_by_doc_name()
                                exit = True
                                break
                            elif col_edit == 'nama pasien':
                                edit_by_patient()
                                exit = True
                                break
                            elif col_edit == 'ruang operasi':
                                edit_by_room()
                                exit = True
                                break
                            elif col_edit == 'nama operasi':
                                edit_by_op_name()
                                exit = True
                                break
                            elif col_edit == 'kode operasi':
                                print('Maaf Anda tidak bisa mengubah Kode Operasi.\n')
                            else:
                                print('Kolom tidak ada.\n')
                    elif edit == 'tidak':
                        break
                    else:
                        print('Mohon hanya masukkan Ya atau Tidak.\n')
            elif edit_option == 0:
                return
            else:
                print('Opsi yang Anda pilih tidak tersedia, silakan masukkan kembali.\n')
        except ValueError:
            print('Input tidak valid, mohon hanya masukkan angka.\n')

def edit_by_doc_id():
    print("""
                      ⚕️ ───── Data Dokter ───── ⚕️
          """)
    doctor_table()
    while True:
        try:
            list_doc_id = [k for k in doctor_data]
            while True:
                edit_doc_id = int(input('Masukkan id dokter baru: '))
                if edit_doc_id in list_doc_id:
                    break
                else:
                    print('Id dokter tidak ditemukan.\n')
                    return
            data_check = None
            for i in operation:
                if i['Kode Operasi'] == op_code:
                    data_check = i
            if data_check:
                op_date = data_check['Tanggal Operasi']
                doc_name = data_check['Nama Dokter']
            doc_date_conflict = False
            while True:
                for i in operation:
                    if [edit_doc_id, op_date] == [i['Id Dokter'], i['Tanggal Operasi']]:
                        doc_date_conflict = True
                if doc_date_conflict:
                    print(f'Dokter {doc_name} memiliki jadwal operasi lain pada tanggal {op_date}.')
                    return
                else:
                    break
            update_data = input('Yakin ingin update data? (Ya/Tidak): ').lower()
            if update_data == 'ya':
                for i in operation:
                    if i['Kode Operasi'] == op_code:
                        i['Id Dokter'] = edit_doc_id
                        i['Nama Dokter'] = doctor_data[edit_doc_id]['Nama Dokter']
                # show_data = [i for i in operation if i['Kode Operasi'] == op_code]
                # print(tabulate(show_data, headers='keys', tablefmt='mixed_outline', numalign='center'))
                print('Data berhasil di-update.')
                print(tabulate(pk_data, headers='keys', tablefmt='mixed_outline', numalign='center'))
                break
            elif update_data == 'tidak':
                break
            else:
                print('Mohon hanya masukkan Ya atau Tidak.\n')
        except ValueError:
            print('Input tidak valid, mohon hanya masukkan angka.\n')

def edit_by_doc_name():
    while True:
        doctor_table()
        list_doc_name = [v['Nama Dokter'] for v in doctor_data.values()]
        while True:
            edit_doc_name = input('Masukkan nama dokter baru: ').title()
            if edit_doc_name in list_doc_name:
                break
            else:
                print('Dokter tidak ditemukan.\n')
                return
        data_check = None
        for i in operation:
            if i['Kode Operasi'] == op_code:
                data_check = i
        if data_check:
            op_date = data_check['Tanggal Operasi']
        doc_date_conflict = False
        while True:
            for i in operation:
                if [edit_doc_name, op_date] == [i['Nama Dokter'], i['Tanggal Operasi']]:
                    doc_date_conflict = True
            if doc_date_conflict:
                print(f'Dokter {edit_doc_name} memilliki jadwal operasi lain pada tanggal {op_date}.')
                return
            else:
                break
        doc_id_store = None
        update_data = input('Yakin ingin update data? (Ya/Tidak): ').lower()
        if update_data == 'ya':
            for k, v in doctor_data.items():
                if v['Nama Dokter'] == edit_doc_name:
                    doc_id_store = k
            for i in operation:
                if i['Kode Operasi'] == op_code:
                    i['Nama Dokter'] = edit_doc_name
                    i['Id Dokter'] = doc_id_store
            # show_data = [i for i in operation if i['Kode Operasi'] == op_code]
            # print(tabulate(show_data, headers='keys', tablefmt='mixed_outline', numalign='center'))
            print('Data berhasil di-update.')
            print(tabulate(pk_data, headers='keys', tablefmt='mixed_outline', numalign='center'))
            break
        elif update_data == 'tidak':
            break
        else:
            print('Mohon hanya masukkan Ya atau Tidak.\n')

def edit_by_patient():
    while True:
        edit_pat_name = input('Masukkan nama pasien baru: ').title()
        update_data = input('Yakin ingin update data? (Ya/Tidak): ').lower()
        if update_data == 'ya':
            for i in operation:
                if i['Kode Operasi'] == op_code:
                    i['Nama Pasien'] = edit_pat_name
            # show_data = [i for i in operation if i['Kode Operasi'] == op_code]
            # print(tabulate(show_data, headers='keys', tablefmt='mixed_outline', numalign='center'))
            print('Data berhasil di-update.')
            print(tabulate(pk_data, headers='keys', tablefmt='mixed_outline', numalign='center'))
            break
        elif update_data == 'tidak':
            break
        else:
            print('Mohon hanya masukkan Ya atau Tidak.\n')

def edit_by_room():
    while True:
        try:
            while True:
                edit_room = int(input('Masukkan ruang operasi baru (1-5): '))
                if edit_room in range(1,6):
                    break
                else:
                    print('Ruang operasi tidak tersedia.\n')
                    return
            data_check = None
            for i in operation:
                if i['Kode Operasi'] == op_code:
                    data_check = i
            if data_check:
                op_date = data_check['Tanggal Operasi']
            date_room_conflict = False
            while True:
                for i in operation:
                    if [op_date, edit_room] == [i['Tanggal Operasi'], i['Ruang Operasi']]:
                        date_room_conflict = True
                if date_room_conflict:
                    print(f'Ruang operasi {edit_room} tidak tersedia pada tanggal {op_date}')
                    return
                else:
                    break
            update_data = input('Yakin ingin update data? (Ya/Tidak): ').lower()
            if update_data == 'ya':
                for i in operation:
                    if i['Kode Operasi'] == op_code:
                        i['Ruang Operasi'] = edit_room
                # show_data = [i for i in operation if i['Kode Operasi'] == op_code]
                # print(tabulate(show_data, headers='keys', tablefmt='mixed_outline', numalign='center'))
                print('Data berhasil di-update.')
                print(tabulate(pk_data, headers='keys', tablefmt='mixed_outline', numalign='center'))
                break
            elif update_data == 'tidak':
                break
            else:
                print('Mohon hanya masukkan Ya atau Tidak.\n')
        except ValueError:
            print('Input tidak valid, mohon hanya masukkan angka.\n')

def edit_by_date():
    while True:
        data_check = None
        for i in operation:
            if i['Kode Operasi'] == op_code:
                data_check = i
                break
        if data_check:
            doc_id = data_check['Id Dokter']
            room = data_check['Ruang Operasi']
            doc_name = data_check['Nama Dokter']
        date_room_conflict = False
        doctor_date_conflict = False
        while True:
            try:
                inp_op_date = input('Masukkan tanggal baru (YYYY-MM-DD): ')
                edit_op_date = datetime.strptime(inp_op_date, '%Y-%m-%d').date()
            except ValueError:
                print('Input tidak valid, mohon masukkan sesuai format (YYYY-MM-DD).')
                continue
            for i in operation:
                if [edit_op_date, room] == [i['Tanggal Operasi'], i['Ruang Operasi']]:
                    date_room_conflict = True
                if [doc_id, edit_op_date] == [i['Id Dokter'], i['Tanggal Operasi']]:
                    doctor_date_conflict = True
            if date_room_conflict:
                print(f'Tanggal {edit_op_date} tidak tersedia untuk ruang operasi {room}.')
                return
            if doctor_date_conflict:
                print(f'Dokter {doc_name} sudah memiliki jadwal operasi lain pada tanggal {edit_op_date}.')
                return
            else:
                break
        update_data = input('Yakin ingin update data? (Ya/Tidak): ').lower()
        if update_data == 'ya':
            for i in operation:
                if i['Kode Operasi'] == op_code:
                    i['Tanggal Operasi'] = edit_op_date
            # show_data = [i for i in operation if i['Kode Operasi'] == op_code]
            # print(tabulate(show_data, headers='keys', tablefmt='mixed_outline', numalign='center'))
            print('Data berhasil di-update.')
            print(tabulate(pk_data, headers='keys', tablefmt='mixed_outline', numalign='center'))
            break
        elif update_data == 'tidak':
            break
        else:
            print('Mohon hanya masukkan Ya atau Tidak.\n')

def edit_by_op_name():
    while True:
        edit_op_name = input('Masukkan nama operasi: ').title()
        update_data = input('Yakin ingin update data? (Ya/Tidak): ').lower()
        if update_data == 'ya':
            for i in operation:
                if i['Kode Operasi'] == op_code:
                    i['Nama Operasi'] = edit_op_name
            # show_data = [i for i in operation if i['Kode Operasi'] == op_code]
            # print(tabulate(show_data, headers='keys', tablefmt='mixed_outline', numalign='center'))
            print('Data berhasil di-update.')
            print(tabulate(pk_data, headers='keys', tablefmt='mixed_outline', numalign='center'))
            break
        elif update_data == 'tidak':
            break
        else:
            print('Mohon hanya masukkan Ya atau Tidak.\n')



# ========== OPTION 4 ========== #
def cancel():
    while True:
        print("""
  ──────────────────────── ✙ ✙ ✙ ────────────────────────
                    SERENITY HOSPITAL
                      CANCEL OPTION
  ───────────────────────────────────────────────────────    
    1. Batalkan Operasi Berdasarkan Kode Operasi
    2. Batalkan Seluruh Operasi
    0. Kembali ke Opsi Utama
⚕️ ─────────────────────────────────────────────────────── ⚕️
              """)
        try:
            cancel_option = int(input('Masukkan opsi yang ingin dijalankan: '))
            if cancel_option == 1:
                del_pk_data()
            elif cancel_option == 2:
                del_all_data()
            elif cancel_option == 0:
                return
            else:
                print('Opsi tidak tersedia, silakan masukkan kembali.\n')
        except ValueError:
            print('Input tidak valid, mohon hanya masukkan angka.\n')

def del_pk_data():
    pk_data_table()
    while True:
        del_option = input('Warning! Data operasi yang dibatalkan akan dihapus dari jadwal.\nApakah Anda yakin ingin membatalkan operasi? (Ya/Tidak): ').lower()
        if del_option == 'ya':
            for i in operation:
                if i['Kode Operasi'] == op_code:
                    operation.remove(i)
            print('Data berhasil dihapus.\n')
            print(tabulate(operation, headers='keys', tablefmt='mixed_outline', numalign='center'))
            return
        elif del_option == 'tidak':
            return
        else:
            print('Mohon hanya masukkan Ya atau Tidak.\n')

def del_all_data():
    while True:
        del_option = input('Warning! Anda akan membatalkan SEMUA operasi, data operasi yang dibatalkan akan dihapus dari jadwal, pastikan Anda benar-benar ingin menghapus semua data.\nApakah Anda yakin ingin menghapus semua data? (Ya/Tidak): ').lower()
        if del_option == 'ya':
            del operation[:]
            print('Data berhasil dihapus.\n')
            print(tabulate(operation, headers=col_name, tablefmt='mixed_outline', numalign='center'))
            return
        elif del_option == 'tidak':
            return
        else:
            print('Mohon hanya masukkan Ya atau Tidak.\n')



op_code = None
col_name = ['Kode Operasi', 'Id Dokter', 'Nama Dokter', 'Nama Pasien', 'Tanggal Operasi', 'Ruang Operasi', 'Nama Operasi']
    
def pk_data_table():
    global op_code
    global pk_data
    op_code_list = [i['Kode Operasi'] for i in operation]
    print(f'\nKode Operasi yang dapat dipilih: {op_code_list}')
    while True:
        op_code = input('\nMasukkan kode operasi: ').upper()
        if op_code.startswith('OP-') and op_code[3:].isdigit():
            break
        else:
            print('Format tidak valid, silakan masukkan kembali.\nFormat: OP-<code>')
    pk_data = [i for i in operation if i['Kode Operasi'] == op_code]
    if pk_data:
        print("""
                                            ⚕️ ───── Jadwal Operasi ───── ⚕️
              """)
        print(tabulate(pk_data, headers='keys', tablefmt='mixed_outline', numalign='center'))
        return True
    else:
        print('Data yang Anda cari tidak ada.\n')
        return False
    
def doctor_table():
    doc_table = [[k, v['Nama Dokter'], v['Departemen'], v['No. Telp']] for k, v in doctor_data.items()]
    print(tabulate(doc_table, headers=['Id Dokter', 'Nama Dokter', 'Departemen', 'No. Telp'], tablefmt='mixed_outline', numalign='center'))

def empty_table():
    print("""
                                            ⚕️ ───── Jadwal Operasi ───── ⚕️
          """)
    print(tabulate([], headers=col_name, tablefmt='mixed_outline', numalign='center'))





# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
mainoption()