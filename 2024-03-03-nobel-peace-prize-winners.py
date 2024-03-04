#!/usr/bin/env python


## 2024/03/04. Levi K. From the blog,
## https://naturallanguagepuzzling.blogspot.com
## This code was written to assist with the 2024/03/03 Sunday Puzzle:
## https://www.npr.org/2024/03/03/1235185763/sunday-puzzle-mountain-house-getaway

"""
This week's challenge: This week's challenge comes from listener Anjali 
Tripathi of Los Angeles, California. Take the last name of a Nobel Peace Prize
winner. Remove the middle three letters and duplicate the last two letters to
get the first name of a different Nobel Peace Prize winner. What are those two
names? Again, take a Nobel Peace Prize winners last name, remove the middle
three letters and duplicate the last two letters, get the first name of another
Nobel Peace Prize winner.
"""


## rough list of Nobel Peace Prize winners-- organizations removed, ".", "-", "Jr." removed.
nobels = [
    'frederic passy', 'henry dunant', 'elie ducommun', 'charles albert gobat',
    'randal cremer', 'bertha felicie sophie von suttner',
    'klas pontus arnoldson', 'fredrik bajer', 'tobias michael carel asser',
    'alfred hermann fried', 'henri la fontaine', 'woodrow wilson',
    'leon victor auguste bourgeois', 'hjalmar branting',
    'christian lous lange', 'fridtjof nansen', 'austen chamberlain',
    'charles gates dawes', 'aristide briand', 'gustav stresemann',
    'ferdinand buisson', 'ludwig quidde', 'frank billings kellogg',
    'nathan soderblom', 'jane addams', 'nicholas murray butler',
    'carl von ossietzky', 'carlos saavedra lamas', 'cordell hull',
    'emily greene balch', 'john raleigh mott', 'ralph bunche',
    'lester bowles pearson', 'albert john lutuli', 'linus pauling',
    'martin luther king', 'rene cassin', 'norman e borlaug',
    'henry kissinger', 'andrei sakharov', 'mairead corrigan',
    'betty williams', 'anwar sadat', 'menachem begin', 'mother teresa',
    'adolfo perez esquivel', 'alva myrdal', 'alfonso garcia robles',
    'lech walesa', 'desmond tutu', 'elie wiesel', 'oscar arias sanchez',
    'tenzin gyatso', 'mikhail gorbachev', 'aung san suu kyi',
    'rigoberta menchu tum', 'nelson mandela', 'fw de klerk',
    'yasser arafat', 'shimon peres', 'yitzhak rabin', 'joseph rotblat',
    'carlos filipe ximenes belo', 'jose ramoshorta', 'jody williams',
    'john hume', 'david trimble', 'kim daejung', 'jimmy carter',
    'shirin ebadi', 'wangari maathai', 'muhammad yunus', 'martti ahtisaari',
    'barack obama', 'liu xiaobo', 'ellen johnson sirleaf', 'leymah gbowee',
    'tawakkol karman', 'malala yousafzai', 'juan manuel santos',
    'denis mukwege', 'nadia murad', 'abiy ahmed', 'maria ressa'
    ]


def transform(winner):
    last = winner.split()[-1]
    if len(last) % 2 == 0:
        pass
    elif len(last) >= 5:
        middle_index = len(last) // 2
        last = last[:middle_index - 1] + last[middle_index + 2:]
        tail = last[-2:]
        last = last+tail
        for n in nobels:
            if n == winner:
                pass
            else:
                first = n.split()[0]
                if first == last:
                    print("MATCH: ", winner, " & ", n)
    else:
        pass


def main():
    for n in nobels:
        transform(n)


if __name__ == "__main__":
    main()

