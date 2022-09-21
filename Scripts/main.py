import csv
data =''
with open('D:/STUDY/ITMO/1_course_ITMO/1_semester(1)/Pyton/Lab-1/books.csv') as csvfile:
    table = csv.reader(csvfile, delimiter = ';')
    cnt = -1
    cntNameMinLenght = 0
    for row in list(table):
        cnt += 1
        if( len(row[1]) > 30):
            cntNameMinLenght += 1
    print('1) Количество строк в файле: ' + str(cnt))
    print('2) Количество строк в файле у которых в поле Название строка длиннее 30 символов: ' + str(cntNameMinLenght))
    searchName = input('3) Поиск по автору: ')
    flag = 0
    with open('D:/STUDY/ITMO/1_course_ITMO/1_semester(1)/Pyton/Lab-1/books.csv') as csvfile2:
        table2 = csv.reader(csvfile2, delimiter=';')
        for row2 in list(table2):
            lower_case2 = row2[3].lower()
            index2 = lower_case2.find(searchName.lower())
            if (index2 != -1):
                date = row2[6]
                dateInt = int(date[0:4])
                if(dateInt > 2016 ):
                    if( dateInt <= 2018):
                        print(row2)
                        flag = 1
        if (flag == 0):
            print('Автор не найден')

    with open('D:/STUDY/ITMO/1_course_ITMO/1_semester(1)/Pyton/Lab-1/books.csv') as csvfile2:
        table3 = csv.reader(csvfile2, delimiter=';')
        f = open('result.txt', 'w')
        cntRow = 0
        for row3 in list(table3):
            if (cntRow != 0):
                f.write(f' {cntRow}) <{row3[3]}>. <{row3[1]}> - <{int(row3[6][0:4])}> \n')
            cntRow += 1
            if (cntRow > 20):
                break
        print('4) 20 книг записаны в текстовый файл')

    tagList = set()
    popularBooks = []
    dic = {}

    print('Дополнитеьное Задание. \n5) Жанры книг, с 16 по 18 год: ')
    with open('D:/STUDY/ITMO/1_course_ITMO/1_semester(1)/Pyton/Lab-1/books.csv') as csvfile2:
        table4 = csv.reader(csvfile2, delimiter=';')
        for row4 in list(table4)[1:]:
            popularBooks.append([int(row4[8]), row4[1], row4[3]])
            date2 = row4[6]
            dateInt = int(date2[0:4])
            if (dateInt > 2016):
                if (dateInt <= 2018):
                    massString = row4[12].split('# ')
                    cntMass = 0
                    for str in massString:
                         tagList.add(massString[cntMass])
                         cntMass += 1
        tagList = list(tagList)
        cnt3 = 0
        for i in tagList:
            print(f'  {cnt3}. {tagList[cnt3]}')
            cnt3 += 1
        cnt3 = 0
        popularBooks.sort(key=lambda x: x[0], reverse=True)
        print('6) Самые популярные книги')
        while cnt3 < 20:
            if(popularBooks[cnt3] != popularBooks[cnt3-1]):
                print(popularBooks[cnt3])
            cnt3 += 1

f.close()








