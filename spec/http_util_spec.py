from expects import *
from src.TargetFile import HttpUtil
from src.TargetFile import StringTools
import mock
import httpretty
import os
with description('StringTools.IsPhoneNumber'):
    with before.each:
        self.st = StringTools()
        
    with it('should return true if is phone number'):
        self.st.GetNumber = mock.Mock(return_value = "13848484848")
        expect(self.st.IsPhoneNumber()).to(be_true)
    
    with it('should return false if is not phone number'):
        self.st.GetNumber = mock.Mock(return_value = "1234")
        expect(self.st.IsPhoneNumber()).to(be_false)

with description('HttpUtil.GetInfo'):
    with before.all:
        httpretty.enable()

    with after.each:
        httpretty.reset()

    with after.all:
        httpretty.disable()
    
    with it('should get auth token from server before get image info'):
        httpretty.register_uri(httpretty.GET, "http://test.com", auth=('user','password'))
        mockModule=mock.patch('src.TargetFile.HttpUtil').start()
        mockModule.GetToken.return_value="token"
        HttpUtil.GetInfo('http://test.com')
        expect(mockModule.GetToken.call_count).to (equal(1))
        mockModule.stop()

    with context('when get token failed'):
        with before.each:
            self.mockModule=mock.patch('src.TargetFile.HttpUtil').start()
            self.mockModule.GetToken.return_value=False
            self.mockEnviron = mock.patch.dict(os.environ,{'USER_NAME':'user', \
                            'PASS_WORD':'password'})
            self.mockEnviron.start()

        with after.each:
            self.mockModule.stop()
            self.mockEnviron.stop()

        with it('should return False'):
            expect(HttpUtil.GetInfo('http://test.com')).to(be_false)

        with it('should not send http request to get info'):
            httpretty.register_uri(httpretty.GET, "http://test.com/images")
            HttpUtil.GetInfo('http://test.com')
            expect(httpretty.has_request()).to(be_false)
    
    with context('when get token success'):
        with before.each:
            self.mockModule=mock.patch('src.TargetFile.HttpUtil').start()
            self.mockModule.GetAuthFromServer.return_value="token"
            self.mockEnviron = mock.patch.dict(os.environ,{'USER_NAME':'user', \
                            'PASS_WORD':'password'})
            self.mockEnviron.start()

        with after.each:
            self.mockModule.stop()
            self.mockEnviron.stop()
        
        with it('will send http request to get info'):
            httpretty.register_uri(httpretty.GET, "http://test.com", auth=('user','password'))
            HttpUtil.GetInfo('http://test.com')
            expect(httpretty.has_request()).to(be_true)
        
        with context('when request of get info failed'):
            with it('should return False'):
                httpretty.register_uri(httpretty.GET, "http://test.com", auth=('user','password'), status=500)
                expect(HttpUtil.GetInfo('http://test.com')).to(be_false)
        
        with context('when request of get info failed'):
            with it('should return info'):
                httpretty.register_uri(httpretty.GET, "http://test.com", auth=('user','password'), status=200)
                expect(HttpUtil.GetInfo('http://test.com')).to(equal(200))
