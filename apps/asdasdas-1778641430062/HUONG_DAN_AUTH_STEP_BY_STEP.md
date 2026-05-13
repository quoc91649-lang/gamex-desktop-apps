# Huong dan he thong Dang ky Dang nhap (Step by Step)

## 1. Muc tieu
Tai lieu nay giup ban giai thich de hieu cach chuong trinh dang ky va dang nhap hoat dong voi file JSON.

## 2. 3 thanh phan chinh
- Giao dien: nhan du lieu nguoi dung nhap vao va hien thong bao.
- Model: xu ly logic dang ky dang nhap.
- Data JSON: noi luu danh sach tai khoan.

## 3. Vai tro tung file
- auth.py: Dieu huong giua man Login/Register, nhan su kien nut bam.
- models/account_models.py: Kiem tra dang nhap, kiem tra trung email, tao tai khoan moi.
- data/data_io.py: Doc va ghi du lieu JSON.
- data/Accounts.json: Danh sach tai khoan that.

## 4. Luong Dang nhap (Step by Step)
1. Nguoi dung nhap email va password o man Dang nhap.
2. Nut Dang nhap goi ham login_account trong auth.py.
3. auth.py goi ham authenticate(email, password) trong model.
4. Model tu dong load lai du lieu moi nhat tu Accounts.json.
5. Model duyet tung tai khoan:
   - Neu email va password dung: tra ve tai khoan.
   - Neu khong tim thay: tra ve None.
6. auth.py hien thong bao:
   - Thanh cong: Dang nhap thanh cong.
   - That bai: Email hoac mat khau khong dung.

## 5. Luong Dang ky (Step by Step)
1. Nguoi dung nhap username, email, password o man Dang ky.
2. Nut Dang ky goi ham register_account trong auth.py.
3. auth.py kiem tra input co rong khong va email co hop le khong.
4. auth.py goi ham add_account(username, email, password) trong model.
5. Model doc danh sach account hien tai tu Accounts.json.
6. Model kiem tra trung email (khong phan biet chu hoa/thuong):
   - Neu trung: tra ve False va thong bao Email da ton tai.
   - Neu khong trung: tiep tuc tao account moi.
7. Model tinh id moi = id lon nhat + 1.
8. Model them account moi vao danh sach.
9. Model ghi lai toan bo danh sach vao Accounts.json.
10. auth.py thong bao Dang ky thanh cong, xoa o nhap, va quay ve man Dang nhap.

## 6. Vi sao cach nay de day lai
- Tach ro tung lop trach nhiem:
  - UI chi giao tiep voi nguoi dung.
  - Model chi xu ly logic.
  - JSON chi luu du lieu.
- Khi loi xay ra, de khoanh vung:
  - Loi giao dien: auth.py.
  - Loi logic: account_models.py.
  - Loi du lieu: Accounts.json hoac data_io.py.

## 7. Checklist test nhanh tren lop
1. Dang nhap dung tai khoan co san trong Accounts.json.
2. Dang nhap sai mat khau de thay thong bao that bai.
3. Dang ky email moi, kiem tra Accounts.json da them dong moi.
4. Dang ky lai cung email, kiem tra thong bao trung email.
5. Dang nhap bang tai khoan vua dang ky.

## 8. Mot cau tom tat de truyen dat
Giao dien nhan input, model xu ly dung/sai, JSON luu ket qua va du lieu tai khoan.
