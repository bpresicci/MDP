# MDP
mdp.py è il file principale, ogni funzione è commentata al suo interno. input.xlsx è troppo grande per essere caricato


16/4/2022 @Benedetta Presicci:
La serie di con Id = 19215652 ha in input i singoli episodi (119), in output resta solo la serie. Non ho controllato se la lista degli attori comprende TUTTI gli attori di tutti gli episodi, ma so che campo Directors diventa NULL così come Subtitles,  il primo non era mai null negli episodi (avevano solo direttori diversi) ed il secondo aveva solo 3 episodi senza sottotoli.
INPUT1 HA 9006 EPI, 8879 MOV, 422 SER
OUTPUT HA 9013 EPI, 8871 MOV, 423 SER
INFATTI 8 EPI DI INPUT SONO DIVENTATI MOV (ID: 19306334, 18968475, 18860725, 6656039, 18968420, 18860716, 18860732, 18860986)

PER ORA IL CHECK_NULL SARà FATTO IGNORANDO 19215652 PERCHè IN QUEI CASI SERVE UN'ANALISI DIVERSA
