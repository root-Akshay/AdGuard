import sqlite3


class logs:

    conn = sqlite3.connect("Logs.db", check_same_thread=False)
    c = conn.cursor()
    i = 1

    # Create table
    try:
        c.execute(
            """CREATE TABLE IF NOT EXISTS logs (Month text,Date int,Time numeric,Type text,IP real,Name text)"""
        )
        c.execute("""CREATE TABLE IF NOT EXISTS blacklists (Month text,Name text)""")
    except:
        pass

    def insert(self, a):
        c = self.c
        try:
            c.execute(
                "INSERT INTO logs VALUES (?,?,?,?,?,?)",
                (a[0], a[1], a[2], a[4], a[7], a[5]),
            )
            c.execute(
                "INSERT INTO blacklists VALUES (?,?)", (a[0] + a[1], a[5]),
            )
        except:
            pass

    def convert(self):
        c = self.c
        conn = self.conn
        data = []
        with open("/var/log/dnsmasq.log") as f:
            for l in f:
                data.append(l.split())

        try:
            c.execute("SELECT max(rowid), * from logs")
            x = c.fetchone()
            x = [*x]
            i = self.i
            for a in data:
                i += 1
                if x[0] is None or i > int(x[0]):
                    self.insert(a)
            conn.commit()
        except Exception as e:
            print(e)
        c.execute("SELECT count(rowid) from logs")
        total = c.fetchone()
        c.execute("SELECT count(*) from logs where IP='0.0.0.0'")
        blocked = c.fetchone()
        c.execute(
            'select type,count(Type) from logs where Type="query[A]" or Type="query[AAAA]" group by Type order by Type asc'
        )
        query_type1 = c.fetchmany(2)
        c.execute(
            'select count(IP),IP from logs where Type="forwarded" and IP!="0.0.0.0" group by IP order by IP desc '
        )
        forwarded = c.fetchmany(2)
        c.execute('select count(Type) from logs where Type="reply"')
        locally = c.fetchone()

        c.execute("select Month,count(Name),Name from blacklists group by Name order by count(Name) desc limit 50")
        blacklists1 = c.fetchall()
        try:
            if forwarded[1][0] == None:
                pass
        except:
            forwarded.append((0, "Secondary DNS"))
        c.execute("select count(Name),Name from logs where IP!='0.0.0.0' group by Name order by count(Name) desc limit 10")
        top10 = c.fetchall()
        return total, blocked, query_type1, forwarded, locally, blacklists1,top10    

    def close(self):
        self.conn.close()


