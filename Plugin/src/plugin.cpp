// JVPLEY ETS2 plugin bootstrap.
// This file deliberately does not pretend to be an SCS telemetry plugin yet.
// The official SCS SDK headers and callback registration must be integrated
// before the DLL can be loaded by ETS2 as a telemetry provider.

#include <windows.h>

extern "C" __declspec(dllexport) const char* JVPLEY_PluginName() {
    return "JVPLEY ETS2 Telemetry";
}

extern "C" __declspec(dllexport) unsigned int JVPLEY_PluginBuild() {
    return 13;
}

BOOL APIENTRY DllMain(HMODULE, DWORD, LPVOID) {
    return TRUE;
}
