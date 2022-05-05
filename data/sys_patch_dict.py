# Dictionary defining patch sets used during Root Volume patching (sys_patch.py)
# Copyright (C) 2022, Mykola Grymalyuk

# Schema for sys_patch_dict.py:
# Supports 3 types of higher level keys:
#  - Install:          Install to root volume      - Dictionary of strings with value of source
#  - Install Non-Root: Install to data partition   - Dictionary of strings with value of source
#  - Remove:           Files to remove             - Array of strings
#  - Processes:        Additional processes to run - Array of strings

# File Storage is based off the origin, ie. '10.13.6/System/Library/Extensions/IOSurface.kext'
# Stubbed binaries are OS specific, they use the 'os_major' variable to denounce which folder to use

from data import os_data

def SystemPatchDictionary(os_major):
    sys_patch_dict = {
        "Graphics": {
            "Non-Metal Common": {
                "Install": {
                    "/System/Library/Extensions": {
                        "IOSurface.kext": "10.15.7",
                    },
                    "/System/Library/Frameworks": {
                        "OpenGL.framework":       "10.14.3",
                        "CoreDisplay.framework": f"10.14.4-{os_major}",
                        "IOSurface.framework":   f"10.15.7-{os_major}",
                        "QuartzCore.framework":  f"10.15.7-{os_major}",
                    },
                    "/System/Library/PrivateFrameworks": {
                        "GPUSupport.framework": "10.14.3",
                        "SkyLight.framework":  f"10.14.6-{os_major}",
                    },
                },
                "Remove": {
                    "/System/Library/Extensions": [
                        "AMDRadeonX4000.kext",
                        "AMDRadeonX4000HWServices.kext",
                        "AMDRadeonX5000.kext",
                        "AMDRadeonX5000HWServices.kext",
                        "AMDRadeonX6000.kext",
                        "AMDRadeonX6000Framebuffer.kext",
                        "AMDRadeonX6000HWServices.kext",
                        "AppleIntelBDWGraphics.kext",
                        "AppleIntelBDWGraphicsFramebuffer.kext",
                        "AppleIntelCFLGraphicsFramebuffer.kext",
                        "AppleIntelHD4000Graphics.kext",
                        "AppleIntelHD5000Graphics.kext",
                        "AppleIntelICLGraphics.kext",
                        "AppleIntelICLLPGraphicsFramebuffer.kext",
                        "AppleIntelKBLGraphics.kext",
                        "AppleIntelKBLGraphicsFramebuffer.kext",
                        "AppleIntelSKLGraphics.kext",
                        "AppleIntelSKLGraphicsFramebuffer.kext",
                        "AppleIntelFramebufferAzul.kext",
                        "AppleIntelFramebufferCapri.kext",
                        "AppleParavirtGPU.kext",
                        "GeForce.kext",
                        "IOAcceleratorFamily2.kext",
                        "IOGPUFamily.kext",
                    ],
                },
                "Install Non-Root": {
                    "/Library/Application Support/SkyLightPlugins": {
                        **({ "DropboxHack.dylib": "SkyLightPlugins" } if os_major >= os_data.os_data.monterey else {}),
                        **({ "DropboxHack.txt": "SkyLightPlugins" } if os_major >= os_data.os_data.monterey else {}),
                    },
                },
            },
            "Metal Common": {
                "Install": {
                    "/System/Library/Frameworks": {
                        "OpenCL.framework": "11.6",
                        "WebKit.framework": "11.6",
                    },
                    "/System/Library/PrivateFrameworks": {
                        "AppleGVA.framework":     "10.15.7",
                        "AppleGVACore.framework": "10.15.7",
                    },
                },
            },

            "Legacy GVA": {
                "Install": {
                    "/System/Library/PrivateFrameworks": {
                        "AppleGVA.framework":     "10.13.6",
                        "AppleGVACore.framework": "10.15.7",
                    },
                },
            },

            "Nvidia Tesla": {
                "Install": {
                    "/System/Library/Extensions": {
                        "GeForceGA.bundle":            "10.13.6",
                        "GeForceTesla.kext":           "10.13.6",
                        "GeForceTeslaGLDriver.bundle": "10.13.6",
                        "GeForceTeslaVADriver.bundle": "10.13.6",
                        "NVDANV50HalTesla.kext":       "10.13.6",
                        "NVDAResmanTesla.kext":        "10.13.6",
                        **({ "NVDAStartup.kext":       "12.0 Beta 6" } if os_major >= os_data.os_data.monterey else {})
                    },
                },
            },
            "Nvidia Kepler": {
                "Install": {
                    "/System/Library/Extensions": {
                        "GeForceAIRPlugin.bundle": "11.0 Beta 3",
                        "GeForceGLDriver.bundle":  "11.0 Beta 3",
                        "GeForceMTLDriver.bundle": "11.0 Beta 3",
                        "GeForce.kext":            "12.0 Beta 6",
                        "GeForceVADriver.bundle":  "12.0 Beta 6",
                        "NVDAGF100Hal.kext":       "12.0 Beta 6",
                        "NVDAGK100Hal.kext":       "12.0 Beta 6",
                        "NVDAResman.kext":         "12.0 Beta 6",
                        "NVDAStartup.kext":        "12.0 Beta 6",
                    },
                },
            },
            "Nvidia Web Drivers": {
                "Install": {
                    "/System/Library/Extensions": {
                        "NVDAStartupWeb.kext":            "10.13.6",
                        "GeForceTeslaWeb.kext":           "10.13.6",
                        "GeForceWeb.kext":                "10.13.6",
                        "NVDAGF100HalWeb.kext":           "10.13.6",
                        "NVDAGK100HalWeb.kext":           "10.13.6",
                        "NVDAGM100HalWeb.kext":           "10.13.6",
                        "NVDAGP100HalWeb.kext":           "10.13.6",
                        "NVDANV50HalTeslaWeb.kext":       "10.13.6",
                        "NVDAResmanTeslaWeb.kext":        "10.13.6",
                        "NVDAResmanWeb.kext":             "10.13.6",
                        "GeForceVADriverWeb.bundle":      "10.13.6",
                        "GeForceAIRPluginWeb.bundle":     "10.13.6",
                        "GeForceGLDriverWeb.bundle":      "10.13.6",
                        "GeForceMTLDriverWeb.bundle":     "10.13.6",
                        "GeForceTeslaGAWeb.bundle":       "10.13.6",
                        "GeForceTeslaGLDriverWeb.bundle": "10.13.6",
                        "GeForceTeslaVADriverWeb.bundle": "10.13.6",
                    },
                },
            },
            "AMD Non-Metal Common": {
                "Install": {
                    "/System/Library/Extensions": {
                        "AMDFramebuffer.kext":           "10.13.6",
                        "AMDLegacyFramebuffer.kext":     "10.13.6",
                        "AMDLegacySupport.kext":         "10.13.6",
                        "AMDShared.bundle":              "10.13.6",
                        "AMDSupport.kext":               "10.13.6",
                    },
                },
                "Remove": {
                    "/System/Library/Extensions": [
                        "AMD7000Controller.kext",
                        "AMD8000Controller.kext",
                        "AMD9000Controller.kext",
                        "AMD9500Controller.kext",
                        "AMD10000Controller.kext",
                    ],
                },
            },

            "AMD TeraScale 1": {
                "Install": {
                    "/System/Library/Extensions": {
                        "AMD2400Controller.kext":        "10.13.6",
                        "AMD2600Controller.kext":        "10.13.6",
                        "AMD3800Controller.kext":        "10.13.6",
                        "AMD4600Controller.kext":        "10.13.6",
                        "AMD4800Controller.kext":        "10.13.6",
                        "ATIRadeonX2000.kext":           "10.13.6",
                        "ATIRadeonX2000GA.plugin":       "10.13.6",
                        "ATIRadeonX2000GLDriver.bundle": "10.13.6",
                        "ATIRadeonX2000VADriver.bundle": "10.13.6",
                    },
                },
            },
            "AMD TeraScale 2": {
                "Install": {
                    "/System/Library/Extensions": {
                        "AMD5000Controller.kext":        "10.13.6",
                        "AMD6000Controller.kext":        "10.13.6",
                        "AMDRadeonVADriver.bundle":      "10.13.6",
                        "AMDRadeonVADriver2.bundle":     "10.13.6",
                        "AMDRadeonX3000.kext":           "10.13.6",
                        "AMDRadeonX3000GLDriver.bundle": "10.13.6",
                        "IOAcceleratorFamily2.kext":     "10.13.6",
                        "IOSurface.kext":                "10.14.6",
                    },
                    "/System/Library/Frameworks": {
                        "OpenCL.framework":    "10.13.6",
                        "IOSurface.framework": f"10.14.6-{os_major}",
                    },
                    "/System/Library/PrivateFrameworks": {
                        "GPUSupport.framework":    "10.13.6",
                        "IOAccelerator.framework": f"10.13.6-{os_major}",
                    },
                },
                "Remove": {
                    "/System/Library/Extensions": [
                        "AppleCameraInterface.kext"
                    ],
                },
            },
            "Intel Ironlake": {
                "Install": {
                    "/System/Library/Extensions": {
                        "AppleIntelHDGraphics.kext":           "10.13.6",
                        "AppleIntelHDGraphicsFB.kext":         "10.13.6",
                        "AppleIntelHDGraphicsGA.plugin":       "10.13.6",
                        "AppleIntelHDGraphicsGLDriver.bundle": "10.13.6",
                        "AppleIntelHDGraphicsVADriver.bundle": "10.13.6",
                    },
                },
            },
            "Intel Sandy Bridge": {
                "Install": {
                    "/System/Library/Extensions": {
                        "AppleIntelHD3000Graphics.kext":           "10.13.6",
                        "AppleIntelHD3000GraphicsGA.plugin":       "10.13.6",
                        "AppleIntelHD3000GraphicsGLDriver.bundle": "10.13.6",
                        "AppleIntelHD3000GraphicsVADriver.bundle": "10.13.6",
                        "AppleIntelSNBGraphicsFB.kext":            "10.13.6",
                        "AppleIntelSNBVA.bundle":                  "10.13.6",
                    },
                },
            },
            "Intel Ivy Bridge": {
                "Processes": {
                    "defaults write com.apple.coremedia hardwareVideoDecoder -string enable": False,
                },
                "Install": {
                    "/System/Library/Extensions": {
                        "AppleIntelHD4000GraphicsGLDriver.bundle":  "11.0 Beta 6",
                        "AppleIntelHD4000GraphicsMTLDriver.bundle": "11.0 Beta 6",
                        "AppleIntelHD4000GraphicsVADriver.bundle":  "11.3 Beta 1",
                        "AppleIntelFramebufferCapri.kext":          "11.4",
                        "AppleIntelHD4000Graphics.kext":            "11.4",
                        "AppleIntelIVBVA.bundle":                   "11.4",
                        "AppleIntelGraphicsShared.bundle":          "11.4", # libIGIL-Metal.dylib pulled from 11.0 Beta 6
                    },
                },
            },
        },
        "Audio": {
            "Legacy Realtek": {
                # For iMac7,1 and iMac8,1 units with legacy Realtek HD Audio
                "Install": {
                    "/System/Library/Extensions": {
                        "AppleHDA.kext":      "10.11.6",
                        "IOAudioFamily.kext": "10.11.6",
                    },
                },
                "Remove": {
                    "/System/Library/Extensions": [
                        "AppleVirtIO.kext",
                        "AppleVirtualGraphics.kext",
                        "AppleVirtualPlatform.kext",
                        "ApplePVPanic.kext",
                        "AppleVirtIOStorage.kext",
                    ],
                },
            },
            # For Mac Pros with non-UGA/GOP GPUs
            "Legacy Non-GOP": {
                "Install": {
                    "/System/Library/Extensions": {
                        "AppleHDA.kext": "10.13.6",
                    },
                },
            },
        },
        "Networking": {
            "Legacy WiFi": {
                "Install": {
                    "/usr/libexec": {
                        "airportd": "11.5.2",
                    },
                    "/System/Library/CoreServices": {
                        "WiFiAgent.app": "11.5.2",
                    },
                },
                "Install Non-Root": {
                    "/Library/Application Support/SkyLightPlugins": {
                        **({ "CoreWLAN.dylib": "SkyLightPlugins" } if os_major >= os_data.os_data.monterey else {}),
                        **({ "CoreWLAN.txt": "SkyLightPlugins" } if os_major >= os_data.os_data.monterey else {}),
                    },
                },
            },
        },
        "Brightness": {
            "Legacy Brightness": {
                "Install": {
                    "/System/Library/Extensions": {
                        "AppleBacklight.kext":       "10.12.6",
                        "AppleBacklightExpert.kext": "10.12.6",
                    },
                    "/System/Library/PrivateFrameworks": {
                        "DisplayServices.framework": "10.12.6",
                    },
                },
                "Remove": {
                    "/System/Library/Extensions/AppleGraphicsControl.kext/Contents/PlugIns": [
                        "AGDCBacklightControl.kext",
                    ],
                },
            },
        },
        "Miscellaneous": {
            "Legacy GMUX": {
                "Install": {
                    "/System/Library/Extensions/AppleGraphicsControl.kext/Contents/PlugIns": {
                        "AppleMuxControl.kext": "10.12.6",
                    },
                },
                "Remove": {
                    "/System/Library/Extensions": [
                        "AppleBacklight.kext",
                    ],
                    "/System/Library/Extensions/AppleGraphicsControl.kext/Contents/PlugIns": [
                        "AGDCBacklightControl.kext",
                        "AppleMuxControl.kext",
                    ],
                },
            },
            "Legacy Keyboard Backlight": {
                "Processes": {
                    "defaults write /Library/Preferences/.GlobalPreferences.plist Moraea_BacklightHack -bool true": True,
                },
            },
        },
    }

    return sys_patch_dict