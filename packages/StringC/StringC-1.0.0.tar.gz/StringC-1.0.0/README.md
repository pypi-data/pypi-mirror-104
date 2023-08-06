# StringC
This Package inherits from str Class   
Attributes:  
    Any string  

# Example:
```
from StringC import StringC
string = StringC("تاریخ برعکس ۱۳۹۹-۱۱-۳۰ تاریخ میلادی 1999/03/02 و تاریخ میلادی برعکس 05/12/95 حروف عربی مثل كيك ۱۳۹۹/۱۱/۳۰ تاریخ")
string.convert
```
# Output:
```
"تاریخ برعکس 1399-11-30 تاریخ میلادی 1999/03/02 و تاریخ میلادی برعکس 05/12/95 حروف عربی مثل کیک 1399/11/30 تاریخ"
```
# dates method
:param content: str  
:return: list of datetime objects  
At the beginning :  
-Any Number in string will convert to En string Number  
-Any Arabic Character in string will convert to Farsi  
For now, it just finds dates in numeric formats which are separated with characters like "-" or "/" or "."  
There is no difference if date is Jalali or Gregorian or Characters are Fa or Ar, this function convert date to  
Gregorian datetime object  
# Example:
```
from StringC import StringC
string = "Today is 1400/01/18"
type(StringC.dates(string))
type(StringC.dates(string)[0])
StringC.dates(string)
```
# Output:
```
<class 'list'>  
<class 'datetime.datetime'>  
[datetime.datetime(2021, 4, 7, 0, 0)] 
```
# Example:
```
from StringC import StringC
string = "today is 2021/04/05"
StringC.dates(string)
```
# Output:
```
[datetime.datetime(2021, 4, 5, 0, 0)]  
```
# Example:
```
from StringC import StringC
string = "today is 2021/04/07 and Today is 1400/01/18 yesterday was 17/01/1400 yesterday also was 06/04/2021"
StringC.dates(string)
```
# Output:
```
[  
datetime.datetime(2021, 4, 7, 0, 0),  
datetime.datetime(2021, 4, 7, 0, 0),  
datetime.datetime(2021, 4, 6, 0, 0),  
datetime.datetime(2021, 4, 6, 0, 0)  
]  
```
# remove_extera_whitespace:
This Function operates on objects convert Property
    And replace more than one white space with one white space
    This Functions also remove any '\n' and any '\t' and instead place one white space
    :return: String Without any '\n' or '\t' Characters

# Example:
```
string = '''
                از کلیه دارندگان واحدهای ممتاز، وکیل یا قائم مقام
                 قانونی صاحبان واحدهای ممتاز و همچنین نماینده و یا نمایندگان اشخاص حقوقی \t \t دعوت میگردد تا
                در جلسه ای که در ساعت12:00مورخ1400/02/27در   نبش بن بست \tمهران\n پلاک ۹۹برگزار می گردد حضور به هم رسانید
                    موضوع :  تصمیم گیری در خصوص تصویب تغییرات و هزینه های صندوق
                    سایر     موارد
                    '''
s = StringC(string)
print(s.remove_extra_whitespace())
```
# Output:
```
از کلیه دارندگان واحدهای ممتاز، وکیل یا قائم مقام قانونی صاحبان واحدهای ممتاز و همچنین نماینده و یا نمایندگان اشخاص حقوقی دعوت میگردد تا در جلسه ای که در ساعت12:00مورخ1400/02/27در نبش بن بست مهران پلاک 99برگزار می گردد حضور به هم رسانید موضوع : تصمیم گیری در خصوص تصویب تغییرات و هزینه های صندوق سایر موارد
```
