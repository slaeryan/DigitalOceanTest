## RunShellcode ##

Simple GUI program when you just want to run some shellcode.

### Tips ###

1. Works on Windows, need Mono port because P/invoke
2. Strips "0x", then any non-hex character (case-insensitive).
3. Add 0xcc at start of shellcode to make it stop in a debugger.
4. Shellcode class can be used in other .NET projects.

![RunShellcode](/screenshot.png?raw=true "RunShellcode")

FAMFAMFAM silk icons CC BY 3.0
