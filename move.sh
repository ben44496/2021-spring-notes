# Move any new files in the home directory to their respective directories
mv 374-* 374/
mv 498dv-* 498dv/
mv 498gc-* 498gc/
mv 211-* 211/
mv 441-* 441/
mv parasol-* parasol/

# Loop through the sub directory scripts and run them
declare -a Scripts=("./374/move.sh ./498dv/move.sh ./498gc/move.sh ./441/move.sh ./211/move.sh ./parasol/move.sh")

for script in ${Scripts[@]}; do
    echo $script
    chmod +x $script
    $script
done
