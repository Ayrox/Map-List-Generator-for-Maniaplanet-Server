import glob
import os
from pick import pick

title = "Choisissez un Mod de Map"
scriptList = ['Chase','Cup','Laps','Rounds','Team','Time Attack']
script, index = pick(scriptList, title, indicator = "=>")

file = open("maplist.txt", "wt")

if script == "Chase":                                               #! Chase
    file.write("""
<?xml version="1.0" encoding="UTF-8"?> 
<playlist> 
    <gameinfos> 
        <game_mode>0</game_mode> 
        <chat_time>10000</chat_time> 
        <finishtimeout>1</finishtimeout> 
        <allwarmupduration>0</allwarmupduration> 
        <disablerespawn>0</disablerespawn> 
        <forceshowallopponents>0</forceshowallopponents> 
        <script_name><![CDATA[Chase.Script.txt]]></script_name> 
    </gameinfos> 
    <filter> 
        <is_lan>1</is_lan> 
        <is_internet>1</is_internet> 
        <is_solo>0</is_solo> 
        <is_hotseat>0</is_hotseat> 
        <sort_index>1000</sort_index> 
        <random_map_order>0</random_map_order> 
    </filter> 
    <script_settings> 
        <setting name="S_ChatTime" type="integer" value="10"/> 
        <setting name="S_UseClublinks" type="boolean" value="0"/> 
        <setting name="S_UseClublinksSponsors" type="boolean" value="0"/> 
        <setting name="S_NeutralEmblemUrl" type="text" value=""/> 
        <setting name="S_ScriptEnvironment" type="text" value="production"/> 
        <setting name="S_MatchmakingAPIUrl" type="text" value="https://v4.live.maniaplanet.com/ingame/public/matchmaking"/> 
        <setting name="S_MatchmakingMatchServers" type="text" value=""/> 
        <setting name="S_MatchmakingMode" type="integer" value="0"/> 
        <setting name="S_MatchmakingRematchRatio" type="real" value="-1"/> 
        <setting name="S_MatchmakingRematchNbMax" type="integer" value="2"/> 
        <setting name="S_MatchmakingVoteForMap" type="boolean" value="0"/> 
        <setting name="S_MatchmakingProgressive" type="boolean" value="0"/> 
        <setting name="S_MatchmakingWaitingTime" type="integer" value="20"/> 
        <setting name="S_LobbyRoundPerMap" type="integer" value="6"/> 
        <setting name="S_LobbyMatchmakerPerRound" type="integer" value="30"/> 
        <setting name="S_LobbyMatchmakerWait" type="integer" value="2"/> 
        <setting name="S_LobbyMatchmakerTime" type="integer" value="8"/> 
        <setting name="S_LobbyDisplayMasters" type="boolean" value="1"/> 
        <setting name="S_LobbyDisableUI" type="boolean" value="0"/> 
        <setting name="S_KickTimedOutPlayers" type="boolean" value="1"/> 
        <setting name="S_MatchmakingErrorMessage" type="text" value="An error occured in the matchmaking API. If the problem persist please try to contact this server administrator."/> 
        <setting name="S_MatchmakingLogAPIError" type="boolean" value="0"/> 
        <setting name="S_MatchmakingLogAPIDebug" type="boolean" value="0"/> 
        <setting name="S_MatchmakingLogMiscDebug" type="boolean" value="0"/> 
        <setting name="S_ProgressiveActivation_WaitingTime" type="integer" value="180000"/> 
        <setting name="S_ProgressiveActivation_PlayersNbRatio" type="integer" value="1"/> 
        <setting name="S_AllowRespawn" type="boolean" value="1"/> 
        <setting name="S_UseLegacyXmlRpcCallbacks" type="boolean" value="1"/> 
        <setting name="S_TimeLimit" type="integer" value="900"/> 
        <setting name="S_MapPointsLimit" type="integer" value="3"/> 
        <setting name="S_RoundPointsLimit" type="integer" value="-5"/> 
        <setting name="S_RoundPointsGap" type="integer" value="3"/> 
        <setting name="S_GiveUpMax" type="integer" value="1"/> 
        <setting name="S_MinPlayersNb" type="integer" value="3"/> 
        <setting name="S_ForceLapsNb" type="integer" value="10"/> 
        <setting name="S_FinishTimeout" type="integer" value="-1"/> 
        <setting name="S_DisplayWarning" type="boolean" value="1"/> 
        <setting name="S_CompetitiveMode" type="boolean" value="0"/> 
        <setting name="S_PauseBetweenRound" type="integer" value="15"/> 
        <setting name="S_WaitingTimeMax" type="integer" value="600"/> 
        <setting name="S_WaypointEventDelay" type="integer" value="500"/> 
        <setting name="S_WarmUpNb" type="integer" value="0"/> 
        <setting name="S_WarmUpDuration" type="integer" value="0"/> 
        <setting name="S_NbPlayersPerTeamMax" type="integer" value="3"/> 
        <setting name="S_NbPlayersPerTeamMin" type="integer" value="3"/> 
    </script_settings> 
    <startindex>0</startindex>
""")
if script == "Cup":                                                 #! Cup
    file.write("""<?xml version="1.0" encoding="UTF-8"?> 
<playlist> 
    <gameinfos> 
        <game_mode>0</game_mode> 
        <chat_time>10000</chat_time> 
        <finishtimeout>1</finishtimeout> 
        <allwarmupduration>0</allwarmupduration> 
        <disablerespawn>0</disablerespawn> 
        <forceshowallopponents>0</forceshowallopponents> 
        <script_name><![CDATA[Cup.Script.txt]]></script_name> 
    </gameinfos> 
    <filter> 
        <is_lan>1</is_lan> 
        <is_internet>1</is_internet> 
        <is_solo>0</is_solo> 
        <is_hotseat>0</is_hotseat> 
        <sort_index>1000</sort_index> 
        <random_map_order>0</random_map_order> 
    </filter> 
    <script_settings> 
        <setting name="S_ChatTime" type="integer" value="10"/> 
        <setting name="S_UseClublinks" type="boolean" value="0"/> 
        <setting name="S_UseClublinksSponsors" type="boolean" value="0"/> 
        <setting name="S_NeutralEmblemUrl" type="text" value=""/> 
        <setting name="S_ScriptEnvironment" type="text" value="production"/> 
        <setting name="S_MatchmakingAPIUrl" type="text" value="https://v4.live.maniaplanet.com/ingame/public/matchmaking"/> 
        <setting name="S_MatchmakingMatchServers" type="text" value=""/> 
        <setting name="S_MatchmakingMode" type="integer" value="0"/> 
        <setting name="S_MatchmakingRematchRatio" type="real" value="-1"/> 
        <setting name="S_MatchmakingRematchNbMax" type="integer" value="2"/> 
        <setting name="S_MatchmakingVoteForMap" type="boolean" value="0"/> 
        <setting name="S_MatchmakingProgressive" type="boolean" value="0"/> 
        <setting name="S_MatchmakingWaitingTime" type="integer" value="20"/> 
        <setting name="S_LobbyRoundPerMap" type="integer" value="6"/> 
        <setting name="S_LobbyMatchmakerPerRound" type="integer" value="30"/> 
        <setting name="S_LobbyMatchmakerWait" type="integer" value="2"/> 
        <setting name="S_LobbyMatchmakerTime" type="integer" value="8"/> 
        <setting name="S_LobbyDisplayMasters" type="boolean" value="1"/> 
        <setting name="S_LobbyDisableUI" type="boolean" value="0"/> 
        <setting name="S_KickTimedOutPlayers" type="boolean" value="1"/> 
        <setting name="S_MatchmakingErrorMessage" type="text" value="An error occured in the matchmaking API. If the problem persist please try to contact this server administrator."/> 
        <setting name="S_MatchmakingLogAPIError" type="boolean" value="0"/> 
        <setting name="S_MatchmakingLogAPIDebug" type="boolean" value="0"/> 
        <setting name="S_MatchmakingLogMiscDebug" type="boolean" value="0"/> 
        <setting name="S_ProgressiveActivation_WaitingTime" type="integer" value="180000"/> 
        <setting name="S_ProgressiveActivation_PlayersNbRatio" type="integer" value="1"/> 
        <setting name="S_AllowRespawn" type="boolean" value="1"/> 
        <setting name="S_UseLegacyXmlRpcCallbacks" type="boolean" value="1"/> 
        <setting name="S_PointsLimit" type="integer" value="100"/> 
        <setting name="S_PointsRepartition" type="text" value=""/> 
        <setting name="S_FinishTimeout" type="integer" value="-1"/> 
        <setting name="S_UseAlternateRules" type="boolean" value="0"/> 
        <setting name="S_ForceLapsNb" type="integer" value="10"/> 
        <setting name="S_DisplayTimeDiff" type="boolean" value="0"/> 
        <setting name="S_RoundsPerMap" type="integer" value="5"/> 
        <setting name="S_NbOfWinners" type="integer" value="3"/> 
        <setting name="S_WarmUpNb" type="integer" value="0"/> 
        <setting name="S_WarmUpDuration" type="integer" value="0"/> 
        <setting name="S_NbOfPlayersMax" type="integer" value="4"/> 
        <setting name="S_NbOfPlayersMin" type="integer" value="4"/> 
    </script_settings> 
    <startindex>0</startindex>
""")
if script == "Laps":                                                #! Laps
    file.write("""<?xml version="1.0" encoding="UTF-8"?>
<playlist> 
    <gameinfos> 
        <game_mode>0</game_mode> 
        <chat_time>10000</chat_time> 
        <finishtimeout>1</finishtimeout> 
        <allwarmupduration>0</allwarmupduration> 
        <disablerespawn>0</disablerespawn> 
        <forceshowallopponents>0</forceshowallopponents> 
        <script_name><![CDATA[Laps.Script.txt]]></script_name> 
    </gameinfos> 
    <filter> 
        <is_lan>1</is_lan> 
        <is_internet>1</is_internet> 
        <is_solo>0</is_solo> 
        <is_hotseat>0</is_hotseat> 
        <sort_index>1000</sort_index> 
        <random_map_order>0</random_map_order> 
    </filter> 
    <script_settings> 
        <setting name="S_ChatTime" type="integer" value="10"/> 
        <setting name="S_UseClublinks" type="boolean" value="0"/> 
        <setting name="S_UseClublinksSponsors" type="boolean" value="0"/> 
        <setting name="S_NeutralEmblemUrl" type="text" value=""/> 
        <setting name="S_ScriptEnvironment" type="text" value="production"/> 
        <setting name="S_AllowRespawn" type="boolean" value="1"/> 
        <setting name="S_UseLegacyXmlRpcCallbacks" type="boolean" value="1"/> 
        <setting name="S_ForceLapsNb" type="integer" value="10"/> 
        <setting name="S_FinishTimeout" type="integer" value="-1"/> 
        <setting name="S_WarmUpNb" type="integer" value="0"/> 
        <setting name="S_WarmUpDuration" type="integer" value="0"/> 
        <setting name="S_TimeLimit" type="integer" value="0"/> 
    </script_settings> 
    <startindex>0</startindex>
""")
if script == "Rounds":                                              #! Rounds
    file.write("""<?xml version="1.0" encoding="UTF-8"?> 
<playlist> 
    <gameinfos> 
        <game_mode>0</game_mode> 
        <chat_time>10000</chat_time> 
        <finishtimeout>1</finishtimeout> 
        <allwarmupduration>0</allwarmupduration> 
        <disablerespawn>0</disablerespawn> 
        <forceshowallopponents>0</forceshowallopponents> 
        <script_name><![CDATA[Rounds.Script.txt]]></script_name> 
    </gameinfos> 
    <filter> 
        <is_lan>1</is_lan> 
        <is_internet>1</is_internet> 
        <is_solo>0</is_solo> 
        <is_hotseat>0</is_hotseat> 
        <sort_index>1000</sort_index> 
        <random_map_order>0</random_map_order> 
    </filter> 
    <script_settings> 
        <setting name="S_ChatTime" type="integer" value="10"/> 
        <setting name="S_UseClublinks" type="boolean" value="0"/> 
        <setting name="S_UseClublinksSponsors" type="boolean" value="0"/> 
        <setting name="S_NeutralEmblemUrl" type="text" value=""/> 
        <setting name="S_ScriptEnvironment" type="text" value="production"/> 
        <setting name="S_AllowRespawn" type="boolean" value="1"/> 
        <setting name="S_UseLegacyXmlRpcCallbacks" type="boolean" value="1"/> 
        <setting name="S_PointsLimit" type="integer" value="50"/> 
        <setting name="S_FinishTimeout" type="integer" value="-1"/> 
        <setting name="S_UseAlternateRules" type="boolean" value="0"/> 
        <setting name="S_ForceLapsNb" type="integer" value="10"/> 
        <setting name="S_DisplayTimeDiff" type="boolean" value="0"/> 
        <setting name="S_RoundsPerMap" type="integer" value="-1"/> 
        <setting name="S_MapsPerMatch" type="integer" value="-1"/> 
        <setting name="S_UseTieBreak" type="boolean" value="1"/> 
        <setting name="S_WarmUpNb" type="integer" value="0"/> 
        <setting name="S_WarmUpDuration" type="integer" value="0"/> 
        <setting name="S_PointsRepartition" type="text" value=""/> 
    </script_settings> 
    <startindex>0</startindex>
""")
if script == "Team":                                                #! Team
    file.write("""<?xml version="1.0" encoding="UTF-8"?> 
<playlist> 
    <gameinfos> 
        <game_mode>0</game_mode> 
        <chat_time>10000</chat_time> 
        <finishtimeout>1</finishtimeout> 
        <allwarmupduration>0</allwarmupduration> 
        <disablerespawn>0</disablerespawn> 
        <forceshowallopponents>0</forceshowallopponents> 
        <script_name><![CDATA[Team.Script.txt]]></script_name> 
    </gameinfos> 
    <filter> 
        <is_lan>1</is_lan> 
        <is_internet>1</is_internet> 
        <is_solo>0</is_solo> 
        <is_hotseat>0</is_hotseat> 
        <sort_index>1000</sort_index> 
        <random_map_order>0</random_map_order> 
    </filter> 
    <script_settings>
        <setting name="S_ChatTime" type="integer" value="10"/> 
        <setting name="S_UseClublinks" type="boolean" value="0"/> 
        <setting name="S_UseClublinksSponsors" type="boolean" value="0"/> 
        <setting name="S_NeutralEmblemUrl" type="text" value=""/> 
        <setting name="S_ScriptEnvironment" type="text" value="production"/> 
        <setting name="S_MatchmakingAPIUrl" type="text" value="https://v4.live.maniaplanet.com/ingame/public/matchmaking"/> 
        <setting name="S_MatchmakingMatchServers" type="text" value=""/> 
        <setting name="S_MatchmakingMode" type="integer" value="0"/> 
        <setting name="S_MatchmakingRematchRatio" type="real" value="-1"/> 
        <setting name="S_MatchmakingRematchNbMax" type="integer" value="2"/> 
        <setting name="S_MatchmakingVoteForMap" type="boolean" value="0"/> 
        <setting name="S_MatchmakingProgressive" type="boolean" value="0"/> 
        <setting name="S_MatchmakingWaitingTime" type="integer" value="20"/> 
        <setting name="S_LobbyRoundPerMap" type="integer" value="6"/> 
        <setting name="S_LobbyMatchmakerPerRound" type="integer" value="30"/> 
        <setting name="S_LobbyMatchmakerWait" type="integer" value="2"/> 
        <setting name="S_LobbyMatchmakerTime" type="integer" value="8"/> 
        <setting name="S_LobbyDisplayMasters" type="boolean" value="1"/> 
        <setting name="S_LobbyDisableUI" type="boolean" value="0"/> 
        <setting name="S_KickTimedOutPlayers" type="boolean" value="1"/> 
        <setting name="S_MatchmakingErrorMessage" type="text" value="An error occured in the matchmaking API. If the problem persist please try to contact this server administrator."/> 
        <setting name="S_MatchmakingLogAPIError" type="boolean" value="0"/> 
        <setting name="S_MatchmakingLogAPIDebug" type="boolean" value="0"/> 
        <setting name="S_MatchmakingLogMiscDebug" type="boolean" value="0"/> 
        <setting name="S_ProgressiveActivation_WaitingTime" type="integer" value="180000"/> 
        <setting name="S_ProgressiveActivation_PlayersNbRatio" type="integer" value="1"/> 
        <setting name="S_AllowRespawn" type="boolean" value="1"/> 
        <setting name="S_UseLegacyXmlRpcCallbacks" type="boolean" value="1"/> 
        <setting name="S_PointsLimit" type="integer" value="50"/> 
        <setting name="S_PointsRepartition" type="text" value=""/> 
        <setting name="S_FinishTimeout" type="integer" value="-1"/> 
        <setting name="S_UseAlternateRules" type="boolean" value="0"/> 
        <setting name="S_ForceLapsNb" type="integer" value="10"/> 
        <setting name="S_DisplayTimeDiff" type="boolean" value="0"/> 
        <setting name="S_MaxPointsPerRound" type="integer" value="6"/> 
        <setting name="S_PointsGap" type="integer" value="1"/> 
        <setting name="S_WarmUpNb" type="integer" value="0"/> 
        <setting name="S_WarmUpDuration" type="integer" value="0"/> 
        <setting name="S_NbPlayersPerTeamMax" type="integer" value="3"/> 
        <setting name="S_NbPlayersPerTeamMin" type="integer" value="3"/> 
    </script_settings> 
    <startindex>0</startindex>
""")
if script == "Time Attack":                                         #! Time Attack
    file.write("""<?xml version="1.0" encoding="UTF-8"?> 
<playlist> 
    <gameinfos> 
        <game_mode>0</game_mode> 
        <chat_time>10000</chat_time> 
        <finishtimeout>1</finishtimeout> 
        <allwarmupduration>0</allwarmupduration> 
        <disablerespawn>0</disablerespawn> 
        <forceshowallopponents>0</forceshowallopponents> 
        <script_name><![CDATA[TimeAttack.Script.txt]]></script_name> 
    </gameinfos> 
    <filter> 
        <is_lan>1</is_lan> 
        <is_internet>1</is_internet> 
        <is_solo>0</is_solo> 
        <is_hotseat>0</is_hotseat> 
        <sort_index>1000</sort_index> 
        <random_map_order>0</random_map_order> 
    </filter> 
    <script_settings>
        <setting name="S_ChatTime" type="integer" value="10"/> 
        <setting name="S_UseClublinks" type="boolean" value="0"/> 
        <setting name="S_UseClublinksSponsors" type="boolean" value="0"/> 
        <setting name="S_NeutralEmblemUrl" type="text" value=""/> 
        <setting name="S_ScriptEnvironment" type="text" value="production"/> 
        <setting name="S_AllowRespawn" type="boolean" value="1"/> 
        <setting name="S_UseLegacyXmlRpcCallbacks" type="boolean" value="1"/> 
        <setting name="S_WarmUpNb" type="integer" value="0"/> 
        <setting name="S_WarmUpDuration" type="integer" value="0"/> 
        <setting name="S_TimeLimit" type="integer" value="300"/> 
    </script_settings> 
    <startindex>0</startindex>
""")

file.close()
file = open("maplist.txt", "a")

dir = []
for path in os.listdir("."):
    if not os.path.isfile(os.path.join(".", path)):
        dir.append(path)

title = "Choisissez le ou les dossiers de maps à ajouter au serveur : "
dirs = pick(dir, title, multiselect = True, min_selection_count = 1, indicator = "=>")

for (x,y) in dirs:
    dir = os.listdir("./" + x)
    
    for map in dir:
        if map.endswith(".Map.Gbx"):
            file.write("""\n    <map>
        <file>"""+ x + "/" + map +"""</file>
    </map>""")

file.write("\n</playlist>")

print("Done")