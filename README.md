# ProjectFullStack2019
Four day full stack 4-7 June 2019 @ Computer Science Thammasat University


## Descriptions
มหาวิทยาลัยธรรมศาสตร์ต้องการสร้างเว็บแอปพลิเคชันสำหรับยืม-คืนหนังสือในห้องสมุดสำหรับนักศึกษาธรรมศาสตร์

## Requirements
- ผู้ใช้ต้องเข้าสู่ระบบก่อนทำการยืมหนังสือเท่านั้น
- หนังสือแต่ละเล่มสามารถยืมได้เพียงคนเดียว
- สามารถแสดงรายชื่อหนังสือทั้งหมดที่มีในระบบได้
- สามารถแสดงรายชื่อหนังสือที่สามารถยืมได้ในระบบได้
- ต้องมีการบันทึก Transactions การยืมคืนหนังสือด้วย
- หนังสือแต่ละเล่มต้องมีองค์ประกอบสำคัญตาม [Base Scheme](#base-schema) _**หมายเหตุ** สามารถเพิ่มองค์ประกอบได้ตามความเหมาะสม_

## Base schema
### Book

| Name      | Type                 |
|-----------|----------------------|
| ID        | PrimaryKey           |
| Title     | CharField            |
| ISBN_10   | CharField            |
| Author    | CharField            |
| Binding   | ForiegnKey           |
| Year      | PositiveSmallInteger |
| Publisher | ForiegnKey           |

**หมายเหตุ** สามารถหาข้อมูลหนังสือเพิ่มเติมได้ที่
- https://isbnsearch.org

### Borrow


| Name | Data Type |
| :--: | :-------: |
|      |           |
| ID | Borrower | Book |
| :--: | :--: | :--: |
| PrimaryKey | ForiegnKey | ForiegnKey |


### Publisher

| ID | Name |
| :---: | :---: |
| PrimaryKey | CharField |

### Binding

| ID | Name |
| :---: | :---: |
| PrimaryKey | CharField |

### Transaction

| ID | Book | Actor | Action | Created  |
| :---: | :---: | :---: | :---: | :---: |
| PrimaryKey | ForiegnKey | ForiegnKey | CharField | DateTimeField |
