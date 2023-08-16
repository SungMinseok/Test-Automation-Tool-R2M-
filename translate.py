import googletrans as gt



def translateTW2KR(targetStr, _srcCode = 'zh-tw', _destCode = 'ko') :
    translator = gt.Translator()
    #translator.()
    #targetStr = str(targetStr).strip()
    #targetStr = str(targetStr).replace('\n','')
    #targetStr = str(input(">:"))
    result = translator.translate(targetStr,src = _srcCode, dest= _destCode)
    if _srcCode == 'zh-tw' :
        result.text = result.text.replace('bind','귀속')
        result.text = result.text.replace('바인딩','귀속')
        result.text = result.text.replace('바인드','귀속')
        result.text = result.text.replace('본드','귀속')
    return result.text

if __name__ == "__main__" : 
    print(translateTW2KR("成空"))