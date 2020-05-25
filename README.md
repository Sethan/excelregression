# excelregression

cut=0
film=()
last_pointer=0
counter=0
for var in "$@"
do 
        if [[ ${var:0:1} == [0-9] ]]
        then    


                if [[ $cut == 1 ]]
                then 
                        cut=0
                        for mov in ${film[@]}
                        do
                                echo "$mov"
                                echo " "$counter".mp4   $last_pointer $var"
                                `./fromTo.sh $mov "$counter"'.mp4' $last_pointer $var`
                        done
                else
                        cut=1
                        last_pointer=$var
                fi

        else  
                film+=( $var )
                echo "eche"
        fi
        counter=$(($counter+1))
done    
echo "$film"
