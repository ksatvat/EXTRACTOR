
def all_lst():
    appdata_list = ['*' , 'APPDATA_', "%APPDATA%", "%AppData%", "%appdata%", "% APPDATA%", "% AppData%", "% appdata%",
                    "<APPDATA>",
                    "<AppData>", "<appdata>",
                    "% APPDATA %", "% AppData %", "% appdata %", "% APPDATA %", "% AppData %", "% appdata %",
                    "< APPDATA >", "%Appdata%",
                    "< AppData >", "< appdata >"]
    common_appdata_list = ['*' ,"%COMMON_APPDATA%", "%common_appdata%", "%Common_Appdata%", "%COMMON_APPDATA%",
                    "%common_appdata%", "%Common_Appdata%" "<COMMON_APPDATA>", "<common_appdata>", "<Common_Appdata>",
                    "% COMMON_APPDATA %", "% common_appdata %", "% Common_Appdata %", "% COMMON_APPDATA %",
                    "% common_appdata %", "% Common_Appdata %" "< COMMON_APPDATA >", "< common_appdata >",
                    "< Common_Appdata >"]

    profilename_list = ['*' ,"PROFILENAME_","%ProfileName%", "%PROFILENAME%", "%Profilename%", "% ProfileName%", "% PROFILENAME%",
                    "% Profilename%", "<ProfileName>", "<PROFILENAME>", "<Profilename>",
                    "% ProfileName %", "% PROFILENAME %", "% Profilename %", "% ProfileName %", "% PROFILENAME %",
                    "% Profilename %", "< ProfileName >", "< PROFILENAME >", "< Profilename >",
                    "%profilename%", "% profilename%","% profilename %", "<profilename>", "< profilename>","< profilename >"]

    username_list = ['*' ,"USERNAME_","%UserName%", "%USERNAME%", "%username%", "% UserName%", "% USERNAME%", "% username%",
                    "<UserName>", "<USERNAME>", "<username>", "<Username>",
                    "% UserName %", "% USERNAME %", "% username %", "% UserName %", "% USERNAME %", "% username %",
                    "< UserName >", "< USERNAME >", "< username >", "< Username >"]

    temp_list = ['*' ,"TEMP_", "%temp%", "%TEMP%", "%Temp%", "% temp%", "% TEMP%",
                    "% Temp%", "<temp>", "<TEMP>", "<Temp>",
                    "% temp %", "% TEMP %", "% Temp %", "% temp %", "% TEMP %",
                    "% Temp %", "< temp >", "< TEMP >", "< Temp >", "<Windows temporary folder>","<temporary folder>" ,"%temporary folder%" ]

    userprofile_list = ['*' , "USERPROFILE_", "%UserProfile%", "%UserProfile%", "%UserProfile%", "%USERPROFILE%","%Userprofile%",
                    "%userprofile%", "<UserProfile>", "<USERPROFILE>", "<userprofile>","<Userprofile>",
                    "% UserProfile%", "% UserProfile%", "% UserProfile%", "% USERPROFILE%","< Userprofile>",
                    "% userprofile%", "< UserProfile>", "< USERPROFILE>", "< userprofile>","< Userprofile >",
                    "% UserProfile %", "% UserProfile %", "% UserProfile %", "% USERPROFILE %","% Userprofile%",
                    "% userprofile %", "< UserProfile >", "< USERPROFILE >", "< userprofile >","% Userprofile %",
                    "% UserProfile %"]

    systemroot_list = ['*' ,"SYSTEMROOT_", "%SystemRoot%", "% SystemRoot %", "% SystemRoot%","%SYSTEMROOT%", "% SYSTEMROOT %", "% SYSTEMROOT%",
                    "%systemroot%", "% systemroot %", "% systemroot%", "%Systemroot%", "% Systemroot %", "% Systemroot%",
                    "<SystemRoot>", "< SystemRoot >", "< SystemRoot>", "<SYSTEMROOT>", "< SYSTEMROOT >","< SYSTEMROOT>",
                    "<systemroot>", "< systemroot >", "< systemroot>", "<Systemroot>", "< Systemroot >","< Systemroot>"]

    windows_list = ['*' , "WINDOWS_","%WINDOWS%", "% WINDOWS %", "% WINDOWS%", "%Windows%", "% Windows %", "% Windows%","%windows%", "% windows %", "% windows%",
                    "<WINDOWS>", "< WINDOWS >", "< WINDOWS>", "<Windows>", "< Windows >", "< Windows>","<windows>", "< windows >", "< windows>"]

    windir_list = ['*' ,"WINDIR_","%WINDIR%", "% WINDIR %", "% WINDIR%", "%Windir%", "% Windir %", "% Windir%", "%windir%","% windir %", "% windir%",
                    "<WINDIR>", "< WINDIR >", "< WINDIR>", "<Windir>", "< Windir >", "< Windir>", "<windir>","< windir >", "< windir>" ]

    defaultuserprofile =['*' ,"DEFAULTUSERPROFILE_", "%DEFAULTUSERPROFILE%", "% DEFAULTUSERPROFILE %", "% DEFAULTUSERPROFILE%",
                    "%defaultuserprofile%", "% defaultuserprofile %", "% defaultuserprofile%",
                    "%Defaultuserprofile%", "% Defaultuserprofile %", "% Defaultuserprofile%",
                    "%DefaultUserProfile%", "% DefaultUserProfile %", "% DefaultUserProfile%",
                    "<DEFAULTUSERPROFILE>", "< DEFAULTUSERPROFILE >", "< DEFAULTUSERPROFILE>",
                    "<defaultuserprofile>", "< defaultuserprofile >", "< defaultuserprofile>",
                    "<Defaultuserprofile>", "< Defaultuserprofile >", "< Defaultuserprofile>",
                    "<DefaultUserProfile>", "< DefaultUserProfile >", "< DefaultUserProfile>"]

    homepath_list = ['*' ,"HOMEPATH_","%HOMEPATH%", "% HOMEPATH %", "% HOMEPATH%",
                    "%HomePath%", "% HomePath %", "% HomePath%",
                    "%homepath%", "% homepath %", "% homepath%",
                    "%Homepath%", "% Homepath %", "% Homepath%",
                    "<HOMEPATH>", "< HOMEPATH >", "< HOMEPATH>",
                    "<HomePath>", "< HomePath >", "< HomePath>",
                    "<homepath>", "< homepath >", "< homepath>",
                    "<Homepath>", "< Homepath >", "< Homepath>"]

    homefolder_list = ['*' ,"HOMEFOLDER_" ,"HOMEFOLDER", "%HOMEFOLDER%", "% HOMEFOLDER %", "% HOMEFOLDER%",
                    "%HomeFolder%", "% HomeFolder %", "% HomeFolder%",
                    "%homefolder%", "% homefolder %", "% homefolder%",
                    "%Homefolder%", "% Homefolder %", "% Homefolder%",
                    "<HOMEFOLDER>", "< HOMEFOLDER >", "< HOMEFOLDER>",
                    "<HomeFolder>", "< HomeFolder >", "< HomeFolder>",
                    "<homefolder>", "< homefolder >", "< homefolder>",
                    "<Homefolder>", "< Homefolder >", "< Homefolder>"]

    programfiles_list = ['*' ,"PROGRAMFILES_", "%PROGRAMFILES%", "% PROGRAMFILES %", "% PROGRAMFILES%",
                    "%ProgramFiles%", "% ProgramFiles %", "% ProgramFiles%",
                    "%programfiles%", "% programfiles %", "% programfiles%",
                    "%Programfiles%", "% Programfiles %", "% Programfiles%",
                    "<PROGRAMFILES>", "< PROGRAMFILES >", "< PROGRAMFILES>",
                    "<ProgramFiles>", "< ProgramFiles >", "< ProgramFiles>",
                    "<programfiles>", "< programfiles >", "< programfiles>",
                    "<Programfiles>", "< Programfiles >", "< Programfiles>"]

    programfile_list = ['*' ,"PROGRAMFILE_", "%PROGRAMFILE%", "% PROGRAMFILE %", "% PROGRAMFILE%",
                    "%ProgramFile%", "% ProgramFile %", "% ProgramFile%",
                    "%programfile%", "% programfile %", "% programfile%",
                    "%Programfile%", "% Programfile %", "% Programfile%",
                    "<PROGRAMFILE>", "< PROGRAMFILE >", "< PROGRAMFILE>",
                    "<ProgramFile>", "< ProgramFile >", "< ProgramFile>",
                    "<programfile>", "< programfile >", "< programfile>",
                    "<Programfile>", "< Programfile >", "< Programfile>"]

    systemfolder_list = ['*' ,"SYSTEMFOLDER_","%SYSTEMFOLDER%", "% SYSTEMFOLDER %", "% SYSTEMFOLDER%",
                        "%SystemFolder%", "% SystemFolder %", "% SystemFolder%",
                        "%systemfolder%", "% systemfolder %", "% systemfolder%",
                        "%Systemfolder%", "% Systemfolder %", "% Systemfolder%",
                        "<SYSTEMFOLDER>", "< SYSTEMFOLDER >", "< SYSTEMFOLDER>",
                        "<SystemFolder>", "< SystemFolder >", "< SystemFolder>",
                        "<systemfolder>", "< systemfolder >", "< systemfolder>",
                        "<Systemfolder>", "< Systemfolder >", "< Systemfolder>",

                         "%SYSTEM FOLDER%", "% SYSTEM FOLDER %", "% SYSTEM FOLDER%",
                         "%System Folder%", "% System Folder %", "% System Folder%",
                         "%system folder%", "% system folder %", "% system folder%",
                         "%System folder%", "% System folder %", "% System folder%",
                         "<SYSTEM FOLDER>", "< SYSTEM FOLDER >", "< SYSTEM FOLDER>",
                         "<System Folder>", "< System Folder >", "< System Folder>",
                         "<system folder>", "< system folder >", "< system folder>",
                         "<System folder>", "< System folder >", "< System folder>"]

    systemdrives_list = ['*' ,"SYSTEMDRIVEs_", "%SYSTEMDRIVEs%", "% SYSTEMDRIVEs %", "% SYSTEMDRIVEs%",
                    "%SystemDrives%", "% SystemDrives %", "% SystemDrives%",
                    "%systemdrives%", "% systemdrives %", "% systemdrives%",
                    "%Systemdrives%", "% Systemdrives %", "% Systemdrives%",
                    "<SYSTEMDRIVEs>", "< SYSTEMDRIVEs >", "< SYSTEMDRIVEs>",
                    "<SystemDrives>", "< SystemDrives >", "< SystemDrives>",
                    "<systemdrives>", "< systemdrives >", "< systemdrives>",
                    "<Systemdrives>", "< Systemdrives >", "< Systemdrives>",
                      "%SYSTEM DRIVEs%", "% SYSTEM DRIVEs %", "% SYSTEM DRIVEs%",
                      "%System Drives%", "% System Drives %", "% System Drives%",
                      "%system drives%", "% system drives %", "% system drives%",
                      "%System drives%", "% System drives %", "% System drives%",
                      "<SYSTEM DRIVEs>", "< SYSTEM DRIVEs >", "< SYSTEM DRIVEs>",
                      "<System Drives>", "< System Drives >", "< System Drives>",
                      "<system drives>", "< system drives >", "< system drives>",
                      "<System drives>", "< System drives >", "< System drives>"
                         "%SYSTEMDRIVE%", "% SYSTEMDRIVE %", "% SYSTEMDRIVE%",
                         "%SystemDRIVE%", "% SystemDRIVE %", "% SystemDRIVE%",
                         "%systemDRIVE%", "% systemDRIVE %", "% systemDRIVE%",
                         "%SystemDRIVE%", "% SystemDRIVE %", "% SystemDRIVE%",
                         "<SYSTEMDRIVE>", "< SYSTEMDRIVE >", "< SYSTEMDRIVE>",
                         "<SystemDRIVE>", "< SystemDRIVE >", "< SystemDRIVE>",
                         "<systemDRIVE>", "< systemDRIVE >", "< systemDRIVE>",
                         "<SystemDRIVE>", "< SystemDRIVE >", "< SystemDRIVE>",
                         "%SYSTEM DRIVE%", "% SYSTEM DRIVE %", "% SYSTEM DRIVE%",
                         "%System DRIVE%", "% System DRIVE %", "% System DRIVE%",
                         "%system DRIVE%", "% system DRIVE %", "% system DRIVE%",
                         "%System DRIVE%", "% System DRIVE %", "% System DRIVE%",
                         "<SYSTEM DRIVE>", "< SYSTEM DRIVE >", "< SYSTEM DRIVE>",
                         "<System DRIVE>", "< System DRIVE >", "< System DRIVE>",
                         "<system DRIVE>", "< system DRIVE >", "< system DRIVE>",
                         ]


    system_list = [ '*' ,"SYSTEM_","%SYSTEM%", "% SYSTEM %", "% SYSTEM%",
                    "%System%", "% System %", "% System%",
                    "%system%", "% system %", "% system%",
                    "<SYSTEM>", "< SYSTEM >", "< SYSTEM>",
                    "<System>", "< System >", "< System>",
                    "<system>", "< system >", "< system>"]

    system32_list = ['*' ,"SYSTEM32_", "%SYSTEM32%", "% SYSTEM32 %", "% SYSTEM32%",
                    "%System32%", "% System32 %", "% System32%",
                    "%system32%", "% system32 %", "% system32%",
                    "<SYSTEM32>", "< SYSTEM32 >", "< SYSTEM32>",
                    "<System32>", "< System32 >", "< System32>",
                    "<system32>", "< system32 >", "< system32>"]

    empty_list = ['*' ,"EMPTY_", "%EMPTY%", "% EMPTY %", "% EMPTY%",
                    "%Empty%", "% Empty %", "% Empty%",
                    "%empty%", "% empty %", "% empty%",
                    "<EMPTY>", "< EMPTY >", "< EMPTY>",
                    "<Empty>", "< Empty >", "< Empty>",
                    "<empty>", "< empty >", "< empty>"]

    random_letters_list = ['*' ,'RANDOM_LETTER', "%RANDOM LETTERS%", "% RANDOM LETTERS %", "% RANDOM LETTERS%",
                    "%Random Letters%", "% Random Letters %", "% Random Letters%",
                    "%random letters%", "% random letters %", "% random letters%",
                    "<RANDOM LETTERS>", "< RANDOM LETTERS >", "< RANDOM LETTERS>",
                    "<Random Letters>", "< Random Letters >", "< Random Letters>",
                    "<random letters>", "< random letters >", "< random letters>",
                    "%RANDOM LETTER%", "% RANDOM LETTER %", "% RANDOM LETTER%",
                    "%Random Letter%", "% Random Letter %", "% Random Letter%",
                    "%random letter%", "% random letter %", "% random letter%",
                    "<RANDOM LETTER>", "< RANDOM LETTER >", "< RANDOM LETTER>",
                    "<Random Letter>", "< Random Letter >", "< Random Letter>",
                    "<random letter>", "< random letter >", "< random letter>",
                    "%RANDOM_LETTERS%", "% RANDOM_LETTERS %", "% RANDOM_LETTERS%",
                    "%Random_Letters%", "% Random_Letters %", "% Random_Letters%",
                    "%random_letters%", "% random_letters %", "% random_letters%",
                    "<RANDOM_LETTERS>", "< RANDOM_LETTERS >", "< RANDOM_LETTERS>",
                    "<Random_Letters>", "< Random_Letters >", "< Random_Letters>",
                    "<random_letters>", "< random_letters >", "< random_letters>",
                    "%RANDOM_LETTER%", "% RANDOM_LETTER %", "% RANDOM_LETTER%",
                    "%Random_Letter%", "% Random_Letter %", "% Random_Letter%",
                    "%random_letter%", "% random_letter %", "% random_letter%",
                    "<RANDOM_LETTER>", "< RANDOM_LETTER >", "< RANDOM_LETTER>",
                    "<Random_Letter>", "< Random_Letter >", "< Random_Letter>",
                    "<random_letter>", "< random_letter >", "< random_letter>"]

    random_numbers_list = ['*' ,'RANDOM_NUMBER', "%RANDOM NUMBERS%", "% RANDOM NUMBERS %", "% RANDOM NUMBERS%",
                    "%Random Numbers%", "% Random Numbers %", "% Random Numbers%",
                    "%random numbers%", "% random numbers %", "% random numbers%",
                    "<RANDOM NUMBERS>", "< RANDOM NUMBERS >", "< RANDOM NUMBERS>",
                    "<Random Numbers>", "< Random Numbers >", "< Random Numbers>",
                    "<random numbers>", "< random numbers >", "< random numbers>",
                    "%RANDOM NUMBER%", "% RANDOM NUMBER %", "% RANDOM NUMBER%",
                    "%Random Number%", "% Random Number %", "% Random Number%",
                    "%random number%", "% random number %", "% random number%",
                    "<RANDOM NUMBER>", "< RANDOM NUMBER >", "< RANDOM NUMBER>",
                    "<Random Number>", "< Random Number >", "< Random Number>",
                    "<random number>", "< random number >", "< random number>",
                    "%RANDOM_NUMBERS%", "% RANDOM_NUMBERS %", "% RANDOM_NUMBERS%",
                    "%Random_Numbers%", "% Random_Numbers %", "% Random_Numbers%",
                    "%random_numbers%", "% random_numbers %", "% random_numbers%",
                    "<RANDOM_NUMBERS>", "< RANDOM_NUMBERS >", "< RANDOM_NUMBERS>",
                    "<Random_Numbers>", "< Random_Numbers >", "< Random_Numbers>",
                    "<random_numbers>", "< random_numbers >", "< random_numbers>",
                    "%RANDOM_NUMBER%", "% RANDOM_NUMBER %", "% RANDOM_NUMBER%",
                    "%Random_Number%", "% Random_Number %", "% Random_Number%",
                    "%random_number%", "% random_number %", "% random_number%",
                    "<RANDOM_NUMBER>", "< RANDOM_NUMBER >", "< RANDOM_NUMBER>",
                    "<Random_Number>", "< Random_Number >", "< Random_Number>",
                    "<random_number>", "< random_number >", "< random_number>"]

    return appdata_list,temp_list,userprofile_list,systemroot_list,profilename_list,username_list,common_appdata_list,random_letters_list,random_numbers_list,systemdrives_list,system32_list,system_list,windir_list,windows_list, empty_list,programfiles_list,programfile_list,defaultuserprofile,homefolder_list,homepath_list
