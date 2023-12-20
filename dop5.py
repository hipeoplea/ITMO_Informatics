import takproto

cot = """<?xml version='1.0' encoding='UTF-8' standalone='yes'?>
<day>
  <lesson>
    <Type id="1">Практика</Type>
    <Name>Линейная алгебра</Name>
    <Start>"11:40"</Start>
    <End>"13:10"</End>
    <Teacher>Гилев Павел</Teacher>
    <Auditory>ауд. 2426, Кронверкский пр., д.49, лит.А</Auditory>
  </lesson>
  <lesson>
    <Type>Лекция</Type>
    <Name>Линейная алгебра</Name>
    <Start>"13:30"</Start>
    <End>"15:00"</End>
    <Teacher>Исаева Татьяна Тимофеевна</Teacher>
    <Auditory>ауд. 1404, Кронверкский пр., д.49, лит.А</Auditory>
  </lesson>
</day>"""
buf = takproto.xml2proto(cot, takproto.TAKProtoVer.STREAM)
print(buf)
outputFile = open('lessons.proto', mode='wb')
outputFile.write(buf)
outputFile.close()
