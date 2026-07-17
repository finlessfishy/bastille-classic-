


set /a titlevar=%RANDOM% %% 100 + 1
set /a titlevar2=%RANDOM% %% 6 + 1

IF titlevar == 100 (
	IF titlevar2 == 1 (
		title purgatory
	) ELSE IF titlevar2 == 2 (
		title hell
	) ELSE IF titlevar2 == 3 (
		title get me out
	) ELSE IF titlevar2 == 4 (
		title help me
	) ELSE IF titlevar2 == 5 (
		title torture
	) ELSE IF titlevar2 == 6 (
		title hell on earth
	)
) ELSE (
	title bastille
)


cd C://

cd %~dp0

main.py
 
REM game closed

pause

