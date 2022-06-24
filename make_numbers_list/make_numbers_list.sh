# Creates a text file "inventory.txt" in an existing folder "inventory" in
# the user's home directory if this file does not already exist and fills it
# with numbers "1:", "2:", ..., "10:", each separated by two newlines.

absolute_filepath="$HOME/inventory/inventory.txt"
number=10

if [ -f $absolute_filepath ]
    then
    echo "The file $absolute_filepath already exists. Do you want to override it [y|n]?"
    read answer
    if [ "$answer" != Y ] && [ "$answer" != y ]
    then
        exit 0
    fi
fi

echo '' > $absolute_filepath # Write a single newline and override existing
                              # content
for((i=1; i<=$number; i++))
do
    echo -e "$i:\n\n" >> $absolute_filepath
done
