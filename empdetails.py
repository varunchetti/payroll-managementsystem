import sqlite3

class Employee:
    def empinsert(self,**k):
        conn = sqlite3.connect('pms.db')
        cur = conn.cursor()
        cur.execute(f''' INSERT INTO EMPLOYEE_DETAILS
                    VALUES({k['eid']},"{k['ename']}",{k['dptid']},
                    "{k['designation']}","{k['email']}",{k['contact']},
                    "{k['address']}")
            ''')
        conn.commit()
    
    def show_employees(self):
        conn = sqlite3.connect('pms.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM EMPLOYEE_DETAILS")
        data = []

        for i in cur.fetchall():
            context = {}
            context['eid'] = i[0]
            context['ename'] = i[1]
            context['dptid'] = i[2]
            context['designation'] = i[3]
            context['email'] = i[4]
            context['contact'] = i[5]
            context['address'] = i[6]
            data.append(context)
        return data

    def attendance(self,**k):
         conn = sqlite3.connect('pms.db')
         cur = conn.cursor()
         cur.execute(f''' INSERT INTO attendance
                    VALUES({k['dptid']},"{k['dptname']}",{k['eid']},
                    "{k['ename']}","{k['date']}","{k['timein']}",
                    "{k['timeout']}")
            ''')
         conn.commit()
    def salaryinsert(self,**k):
        conn = sqlite3.connect('pms.db')
        cur = conn.cursor()
        cur.execute(f''' INSERT INTO sallary_details
                    VALUES({k['eid']},{k['dptid']},{k['account_number']},
                    {k['pan']},{k['base_sallary']})
            ''')
        conn.commit()

class SalaryCalculator:
    def salarycalculation(self,eid):
        conn=sqlite3.connect('pms.db')
        cur=conn.cursor()
        cur.execute(f"select base_sallary from sallary_details where EID={eid}")
        bs=cur.fetchall()[0][0]
        cur.execute(f"select date,timein,timeout from attendance where EID={eid}")
        gt=cur.fetchall()
        print(bs)
        print(gt)
        hrs=bs/(22*8)
        su=0
        for i in gt:
            g=(int(i[2][:2])-int(i[1][:2]))*hrs
            su=su+g
        return su