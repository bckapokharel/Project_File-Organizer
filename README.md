#Project File Organizer
 
This project  automatically sorts and organizes files into categorized folders based on their extensions. This tool helps maintain a clean and organized directory by grouping files into specific categories such as images, documents, videos, and more.

#Features

a)Automatically categorizes files into pre-defined folders. 

b)Supports a wide range of file types (images, documents, videos, audio, etc.). 

c)Customizable to handle additional file types or categories. 

d)Handles both current and specified directories. 


#Table of Contents

i)Installation 

ii)Usage 

iii)Configuration 

iv)Example 

v)Contributing 


#Installation 

Requirements 

#Python 3.x


*Steps 

-Clone the repository:

git clone https://github.com/your-username/file-organizer.git
cd file-organizer

-Install dependencies (if any):

pip install -r requirements.txt 

#Usage

*Basic Usage

1)Place the script in the directory you want to organize. 

2)Run the script: 

python file_organizer.py 


Organize a Specific Directory

You can specify a target directory as an argument:

python file_organizer.py /path/to/directory


#Configuration

We can customize the folder categories and file extensions by modifying the FILE_TYPE_MAPPING dictionary in the file_organizer.py file. For example: 

FILE_TYPE_MAPPING = {

    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    
    "Documents": [".pdf", ".docx", ".txt"],
    
    "Videos": [".mp4", ".mkv", ".avi"],
    
    "Audio": [".mp3", ".wav"],
    
    "Archives": [".zip", ".rar", ".7z"],
    
}


#Example 

*Before Running 

/Downloads 

  ├── image1.jpg 
  
  ├── document1.pdf 
  
  ├── song.mp3 
  
  ├── movie.mp4 
  
  
*After Running 

/Downloads 

  ├── Images 
  
  │    └── image1.jpg 
  
  ├── Documents 
  
  │    └── document1.pdf 
  
  ├── Audio 
  
  │    └── song.mp3 
  
  ├── Videos 
  
       └── movie.mp4 
       
       
       
#Contributing

To contribute: 

a)Fork the repository. 

b)Create a new branch:

git checkout -b feature-name 

c)Make your changes and commit them: 

git commit -m "Add feature-name" 

d)Push your branch: 

git push origin feature-name 

e)Open a pull request. 


#Acknowledgments

I want to give Special thanks to the Upskills Campus tp give me special opportunity to make a project on File Organizer.

