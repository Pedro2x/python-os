import os, sys
#1. Open the filenames.txt file with read-only access with the open() function

filename = 'filenames.txt'
file = open(filename, 'r')


#2. Print the name of the file and if it is open or closed using the .name and .closed properties

print(file.name)
print(file.closed)

#3. Use a for loop to read all lines of filenames.txt into a list variable

list = []

for line in file:
   list.append(line)




#4. Print out all the lines from the file from your variable

print(list)

#5. Close the filenames.txt file and print if the file is open or closed

file.close()
print(file.closed)

#6. Create a file using the open() function called secrets.txt

file = open('secrets.txt', 'w+')




#7. Write your own secrets to the file with the write() function

file.write('gotta study the stuff')
file.write(' this is the best')
file.write(' and it is paved over')


#8. Close the secrets.txt file using the close() method. DON'T FORGET!

file.close()


#9. Print out the contents of the text file in your terminal to prove it worked
print(open('secrets.txt').read())

#10. Open your secrets.txt file in append mode and write some more super secret info
file = open('secrets.txt', 'a')
file.write('\n syntax is a challenge to learn')
#11. Close the secrets.txt file again using the close() function
file.close()
#12. Rename the secrets.txt and make it a "hidden" file named .supersecret.txt using the os.rename() function

os.rename('secrets.txt', '.supersecret.txt')

#13. See if you can see the file in your file explorer

# I DO NOT SEE THE FILE IN FILE EXPLORER

#14. Create a list variable named file_names that contains a list of filenames

file_names= ['\nangelfile.txt' ,  '\nhistory1940.doc' , '\ntest.py.html.css.txt']

#15. Use the writelines() function to append the filenames to the filenames.txt file

file = open('filenames.txt' , 'a')
file.writelines(file_names)

#16. Delete the initial secrets.txt file now that you have a super secret hidden version

os.remove('.supersecret.txt')

#17. BOSS LEVEL: Use the input() function to accept user input of a filename to create and create that file.
