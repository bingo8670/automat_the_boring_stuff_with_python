#-*- coding: UTF-8 -*-
from selenium import webdriver
import time


#函数名称： LoginFun(_driver,_emailAddress,_username,_password)
#函数功能： 实现根据指定QQ邮箱网页，账号，密码实现登陆QQ邮箱动作
#输入参数： _driver：webdirver模块初始化Firfox对象？  
#                 _emailAddress：访问QQ邮箱网址
#                 _username:邮箱用户名
#                 _password:相应邮箱用户名密码
#输出参数： 从新定位的driver对象
#修改信息:   2018-05-12  QiYe005
def LoginFun(_driver,_emailAddress,_username,_password):
    print ("尝试登陆qq邮箱网址")
    #登录网址
    _driver.get(_emailAddress)
    #尝试账号密码方式登录
    _driver.switch_to_frame("login_frame");  
    loginByUserLink = _driver.find_element_by_link_text("帐号密码登录");  
    loginByUserLink.click();  
    username = _driver.find_element_by_id("u");  
    password = _driver.find_element_by_id("p");  
    loginbutton = _driver.find_element_by_id("login_button");
    print ("尝试输入账号密码并登陆")
    #输入账号密码
    username.clear();  
    password.clear();  
    username.send_keys(_username);  
    password.send_keys(_password);  
    loginbutton.click();  
    print ("账号密码登陆按钮已点击")
    _driver.implicitly_wait(5)


#函数名称      WriteAndSendFun(_driver,_receiverAddress,_subjectString,_contentString)
#函数功能：   实现根据指定收件人定制，主题，新建邮件正文内容，实现填写及发送动作
#输入参数：   _driver：webdirver模块初始化Firfox对象？  
#                   _receiverAddress：收件人邮箱
#                   _subjectString:主题名称
#                   _contentString:邮件正文内容
#输出参数：   从新定位的driver对象
#修改信息:    2018-05-12  QiYe005
def WriteAndSendFun(_driver,_receiverAddress,_subjectString,_contentString):
    #转自：https://blog.csdn.net/vae0000/article/details/73162662
    _driver.switch_to_default_content()  
    writeLink = _driver.find_element_by_link_text("写信");  
    writeLink.click();  
    #切换到写信框架
    _driver.switch_to_frame("mainFrame");  
    #收信人信息
    toUser = _driver.find_element_by_xpath(".//*[@id='toAreaCtrl']/div[2]/input");
    toUser.send_keys(_receiverAddress)
    #邮件主题信息
    title = _driver.find_element_by_id("subject");  
    title.send_keys(_subjectString);
    #邮件正文信息
    _driver.switch_to_frame(_driver.find_element_by_tag_name("iframe"));
    content = _driver.find_element_by_tag_name("body");
    content.send_keys(_contentString);
    #送信按钮触发
    _driver.switch_to.parent_frame();  
    sendButton = _driver.find_element_by_link_text("发送");
    sendButton.click();
    print ("邮件内容已经填写完毕并触发“发送按钮”")
    _driver.implicitly_wait(5)

#函数名称      LogoutFun(_driver)直接关闭浏览器退出
#函数功能：   实现退出操作，原来发送邮件后页面自动跳转，想定位到退出按钮失败，还是太年轻了
#输入参数：   _driver：webdirver模块初始化Firfox对象？  
#输出参数：   无
#修改信息:      2018-05-12  QiYe005
def LogoutFun(_driver):
    #退出操作
    #driver.switch_to_frame("actionFrame")
    #logoutLink = driver.find_element_by_link_text("退出");
    #logoutLink.click()
    #time.sleep(3)
    print("最后退出邮件")
    #按照顺序来的，应该不用定义函数了吧   
    _driver.close()
    
#定义主函数
def main():
    #驱动存放位置
    webDriverLoc=r'C:\bin\geckodriver.exe'
    driver = webdriver.Firefox(executable_path=webDriverLoc)
    #QQ邮箱网址，账号密码相关
    emailAddress="https://mail.qq.com/"
    username='登陆邮箱账号'
    password='登陆邮箱密码'
    #邮件内容定义
    receiverAddress="收件人邮箱"
    subjectString="selenup+python自动化测试"
    contentString="这是邮件正文，测试，测试"
    #调用登陆操作子函数
    LoginFun(driver,emailAddress,username,password)
    #调用写信与发送操作子函数
    WriteAndSendFun(driver,receiverAddress,subjectString,contentString)
    #最后调用退出操作子函数
    LogoutFun(driver)
#调用主函数
if __name__ == "__main__":
     main()    
