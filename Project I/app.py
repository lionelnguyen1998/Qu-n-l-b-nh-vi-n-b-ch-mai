
import sqlite3

from flask import Flask, render_template,url_for

app = Flask(__name__)


@app.route('/')
def search():
    return render_template('form.html')

@app.route('/BenhDaNhiemKhuan',methods=['POST','GET'])
def BenhDaNhiemKhuan():
    return render_template('BenhDaNhiemKhuan.html')

@app.route('/BenhNoiTiet',methods=['POST','GET'])
def BenhNoiTiet():
    return render_template('BenhNoiTietVaDaiThaoDuong.html')

@app.route('/BenhVeMat',methods=['POST','GET'])
def BenhVeMat():
    return render_template('BenhVeMat.html')

@app.route('/TheoYeuCau',methods=['POST','GET'])
def TheoYeuCau():
    return render_template('TheoYeuCau.html')

@app.route('/XuongKhop',methods=['POST','GET'])
def XuongKhop():
    return render_template('XuongKhop.html')

@app.route('/BenhVienNhietDoi',methods=['POST','GET'])
def BenhVienNhietDoi():
    return render_template('BenhVienNhietDoi.html')

@app.route('/Motsoquytrinhkhambenh',methods=['POST','GET'])
def Motsoquytrinhkhambenh():
    return render_template('Motsoquytrinhkhambenh.html')


@app.route('/Quytrinhkhamxuongkhop',methods=['POST','GET'])
def Quytrinhkhamxuongkhop():
    return render_template('Quytrinhkhamxuongkhop.html')

@app.route('/Quytrinhkhambenhtheoyeucau',methods=['POST','GET'])
def Quytrinhkhambenhtheoyeucau():
    return render_template('Quytrinhkhambenhtheoyeucau.html')

@app.route('/Quytrinhkhambenhnhietdoi',methods=['POST','GET'])
def Quytrinhkhambenhnhietdoi():
    return render_template('Quytrinhkhambenhnhietdoi.html')

@app.route('/CanLamSang',methods=['POST','GET'])
def CanLamSang():
    # step 1: connect to db
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    # step 2: create a cursor
    cur = conn.cursor()
    # step 3: execute SQL statement
    cur.execute('''select * from CacKhoaCanLamSang''')
    # step 4: fetch
    rows = cur.fetchall()
    # print(rows)
    return render_template('header_Khoa.html', rows=rows)

@app.route('/LamSang',methods=['POST','GET'])
def LamSang():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute('''select * from CacKhoaLamSang''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)


@app.route('/Vien',methods=['POST','GET'])
def Vien():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute('''select * from CacVien''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/TrungTam',methods=['POST','GET'])
def TrungTam():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute('''select * from TrungTamTrucThuoc''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/ChucNang',methods=['POST','GET'])
def ChucNang():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute('''select * from PhongChucNang''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhoaDaLieu',methods=['POST','GET'])
def KhoaDaLieu():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khoa da liễu%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhoaNoiTietVaDaiThaoDuong',methods=['POST','GET'])
def KhoaNoiTietVaDaiThaoDuong():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khoa Nột tiết và Đái tháo đường%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhoaMat',methods=['POST','GET'])
def KhoaMat():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khoa Mắt%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhamChuaBenhTheoYeuCau',methods=['POST','GET'])
def KhamChuaBenhTheoYeuCau():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khoa Khám chữa bệnh theo yêu cầu%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhoaCoXuongKhop',methods=['POST','GET'])
def KhoaCoXuongKhop():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khoa cơ xương khớp%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhoaCapCuu',methods=['POST','GET'])
def KhoaCapCuu():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khoa cấp cứu%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhoaChanThuong',methods=['POST','GET'])
def KhoaChanThuong():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khao chấn thương chỉnh hình và cột sống%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhoaGayMe',methods=['POST','GET'])
def KhoaGayMe():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khoa Gây mê hồi sức%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhoaHoiSuc',methods=['POST','GET'])
def KhoaHoiSuc():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khoa Hồi sức tích cực%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhoaNgoai',methods=['POST','GET'])
def KhoaNgoai():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khoa Ngoại tổng hợp%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhoaNhi',methods=['POST','GET'])
def KhoaNhi():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khoa Nhi%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhoaPhauThuat',methods=['POST','GET'])
def KhoaPhauThuat():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khoa Phẫu thuật thần kinh%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhoaPhuSan',methods=['POST','GET'])
def KhoaPhuSan():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khoa Phụ sản%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhoaRangHamMat',methods=['POST','GET'])
def KhoaRangHamMat():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khoa Răng hàm mặt%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhoaTaiMuiHong',methods=['POST','GET'])
def KhoaTaiMuiHong():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khoa Tai Mũi Họng%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhoaThanKinh',methods=['POST','GET'])
def KhoaThanKinh():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khoa Thần kinh%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhoaThanNhanTao',methods=['POST','GET'])
def KhoaThanNhanTao():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khoa Thận nhân tạo%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhoaThanTietNieu',methods=['POST','GET'])
def KhoaThanTietNieu():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khoa Thận tiết niệu%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhoaTieuHoa',methods=['POST','GET'])
def KhoaTieuHoa():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khoa tiêu hóa%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/KhoaYHocCoTruyen',methods=['POST','GET'])
def KhoaYHocCoTruyen():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaLamSang where TenKhoa like '%Khoa y học cổ truyền%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)


@app.route('/KhoaHoaSinh',methods=['POST','GET'])
def KhoaHoaSinh():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaCanLamSang where TenKhoa like '%Khoa Hóa sinh%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)


@app.route('/KhoaThamDoChucNang',methods=['POST','GET'])
def KhoaThamDoChucNang():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaCanLamSang where TenKhoa like '%Khoa Thăm dò chức năng%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)


@app.route('/KhoaViSinh',methods=['POST','GET'])
def KhoaViSinh():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacKhoaCanLamSang where TenKhoa like '%Khoa Vi sinh%' ''')
    rows = cur.fetchall()
    return render_template('header_Khoa.html', rows=rows)

@app.route('/GiamDinhYKhoa',methods=['POST','GET'])
def GiamDinhYKhoa():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacVien where TenVien like '%Viện giám định y khoa%' ''')
    rows = cur.fetchall()
    return render_template('header_Vien.html', rows=rows)

@app.route('/TamThan',methods=['POST','GET'])
def TamThan():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacVien where TenVien like '%Viện sức khỏe tâm thần%' ''')
    rows = cur.fetchall()
    return render_template('header_Vien.html', rows=rows)

@app.route('/TimMach',methods=['POST','GET'])
def TimMach():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from CacVien where TenVien like '%Viện Tim mạch%' ''')
    rows = cur.fetchall()
    return render_template('header_Vien.html', rows=rows)

@app.route('/TTBenhVienNhietDoi',methods=['POST','GET'])
def TTBenhVienNhietDoi():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from TrungTamTrucThuoc where TenTrungTam like '%Trung tâm bệnh viện nhiệt đới%' ''')
    rows = cur.fetchall()
    return render_template('header_Vien.html', rows=rows)

@app.route('/TTChongDoc',methods=['POST','GET'])
def TTChongDoc():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from TrungTamTrucThuoc where TenTrungTam like '%Trung tâm Chống độc%' ''')
    rows = cur.fetchall()
    return render_template('header_TrungTam.html', rows=rows)

@app.route('/TTDaoTaoChiDaoTuyen',methods=['POST','GET'])
def TTDaoTaoChiDaoTuyen():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from TrungTamTrucThuoc where TenTrungTam like '%Trung tâm Đào tạo_Chỉ đạo tuyến%' ''')
    rows = cur.fetchall()
    return render_template('header_TrungTam.html', rows=rows)

@app.route('/TTDiUngMienDichLamSang',methods=['POST','GET'])
def TTDiUngMienDichLamSang():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from TrungTamTrucThuoc where TenTrungTam like '%Trung tâm Dị ứng Miễn dịch Lâm sàng%' ''')
    rows = cur.fetchall()
    return render_template('header_TrungTam.html', rows=rows)

@app.route('/TTDienQuang',methods=['POST','GET'])
def TTDienQuang():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from TrungTamTrucThuoc where TenTrungTam like '%Trung tâm điện quang%' ''')
    rows = cur.fetchall()
    return render_template('header_TrungTam.html', rows=rows)

@app.route('/TTDinhDuongLamSang',methods=['POST','GET'])
def TTDinhDuongLamSang():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from TrungTamTrucThuoc where TenTrungTam like '%Trung tâm Dĩnh dương lâm sàng%' ''')
    rows = cur.fetchall()
    return render_template('header_TrungTam.html', rows=rows)

@app.route('/TTGiaiPhauBenh',methods=['POST','GET'])
def TTGiaiPhauBenh():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from TrungTamTrucThuoc where TenTrungTam like '%Trung tâm giải phẫu bệnh%' ''')
    rows = cur.fetchall()
    return render_template('header_TrungTam.html', rows=rows)

@app.route('/TTHoHap',methods=['POST','GET'])
def TTHoHap():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from TrungTamTrucThuoc where TenTrungTam like '%Trung tâm hô hấp%' ''')
    rows = cur.fetchall()
    return render_template('header_TrungTam.html', rows=rows)

@app.route('/TTHuyetHocVaTruyenMau',methods=['POST','GET'])
def TTHuyetHocVaTruyenMau():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from TrungTamTrucThuoc where TenTrungTam like '%Trung tâm huyết học và truyền máu%' ''')
    rows = cur.fetchall()
    return render_template('header_TrungTam.html', rows=rows)

@app.route('/TTPhucHoiChucNang',methods=['POST','GET'])
def TTPhucHoiChucNang():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from TrungTamTrucThuoc where TenTrungTam like '%Trung tâm phục hồi chức năng%' ''')
    rows = cur.fetchall()
    return render_template('header_TrungTam.html', rows=rows)

@app.route('/PBaoVe',methods=['POST','GET'])
def PBaoVe():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from PhongChucNang where TenPhong like '%Phòng Bảo vệ ANTT%' ''')
    rows = cur.fetchall()
    return render_template('header_Phong.html', rows=rows)

@app.route('/PCNTT',methods=['POST','GET'])
def PCNTT():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from PhongChucNang where TenPhong like '%Phòng công nghệ thông tin%' ''')
    rows = cur.fetchall()
    return render_template('header_Phong.html', rows=rows)

@app.route('/PCTXH',methods=['POST','GET'])
def PCTXH():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from PhongChucNang where TenPhong like '%Phòng công tác xã hội %' ''')
    rows = cur.fetchall()
    return render_template('header_Phong.html', rows=rows)

@app.route('/PDieuDuong',methods=['POST','GET'])
def PDieuDuong():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from PhongChucNang where TenPhong like '%Phòng điều dưỡng%' ''')
    rows = cur.fetchall()
    return render_template('header_Phong.html', rows=rows)

@app.route('/PDoiNgoaiVaHopTacQuocTe',methods=['POST','GET'])
def PDoiNgoaiVaHopTacQuocTe():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from PhongChucNang where TenPhong like '%Phòng đối ngoại và hợp tác quốc tế%' ''')
    rows = cur.fetchall()
    return render_template('header_Phong.html', rows=rows)

@app.route('/PHanhChinhQuanTri',methods=['POST','GET'])
def PHanhChinhQuanTri():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from PhongChucNang where TenPhong like '%Phòng hành chính quản trị%' ''')
    rows = cur.fetchall()
    return render_template('header_Phong.html', rows=rows)

@app.route('/PKeHoachTongHop',methods=['POST','GET'])
def PKeHoachTongHop():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from PhongChucNang where TenPhong like '%Phòng kế hoạch tổng hợp%' ''')
    rows = cur.fetchall()
    return render_template('header_Phong.html', rows=rows)

@app.route('/PNghiemCuuKhoaHoc',methods=['POST','GET'])
def PNghiemCuuKhoaHoc():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from PhongChucNang where TenPhong like '%Phòng Nghiêm cứu khoa học%' ''')
    rows = cur.fetchall()
    return render_template('header_Phong.html', rows=rows)

@app.route('/PQuanLyChatLuong',methods=['POST','GET'])
def PQuanLyChatLuong():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from PhongChucNang where TenPhong like '%Phòng quản lý chất lượng%' ''')
    rows = cur.fetchall()
    return render_template('header_Phong.html', rows=rows)

@app.route('/PTaiChinhKeToan',methods=['POST','GET'])
def PTaiChinhKeToan():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from PhongChucNang where TenPhong like '%Phòng Tài chính kế toán%' ''')
    rows = cur.fetchall()
    return render_template('header_Phong.html', rows=rows)

@app.route('/PToChucCanBo',methods=['POST','GET'])
def PToChucCanBo():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from PhongChucNang where TenPhong like '%Phòng tổ chức cán bộ%' ''')
    rows = cur.fetchall()
    return render_template('header_Phong.html', rows=rows)

@app.route('/PVatTuThietBiYTe',methods=['POST','GET'])
def PVatTuThietBiYTe():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from PhongChucNang where TenPhong like '%Phòng Vật tư thiết bị y tế%' ''')
    rows = cur.fetchall()
    return render_template('header_Phong.html', rows=rows)

@app.route('/TTTBenhVienNhietDoi',methods=['POST','GET'])
def TTTBenhVienNhietDoi():
    conn = sqlite3.connect('QLyBenhVienBachMai.db')
    cur = conn.cursor()
    cur.execute(''' select * from TrungTamTrucThuoc where TenTrungTam like '%Trung tâm bệnh viện nhiệt đới%' ''')
    rows = cur.fetchall()
    return render_template('header_Phong.html', rows=rows)



if __name__ == '__main__':
    app.run(debug=True)