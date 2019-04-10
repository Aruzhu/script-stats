git shortlog -s | cut -c8- > user.txt
echo "" > out.txt
while read p; do
	git log --shortstat --author="$p" | grep -E "fil(e|es) changed" | awk '{files+=$1; inserted+=$4; deleted+=$6} END {print "files changed: ", files, "lines inserted: ", inserted, "lines deleted: ", deleted }' >> out.txt
	echo "" >> out.txt
done < user.txt
git shortlog -s -a | cut -c8-
echo "running python"
"C:/Python27/python.exe" parse.py