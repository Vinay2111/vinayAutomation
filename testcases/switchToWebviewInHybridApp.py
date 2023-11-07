'''in the normal app we can switch to any webview page like google and perform any automation, so we need to try to use switch to method'''


#example

webcontext = driver.contexts

for context in webcontext:
    print(context)

#after running this we will get different context , eg: native app, WEBVIEW_chrome etc,
#now use this context to automate by using "Switch to" method

driver.switch_to_context("WEBVIEW_chrome")

#then use normal methods like

driver.find_elements(by.xpath,"dhbhjdshjd").sendkeys("hbdhbsd") #now the search will work