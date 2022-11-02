# ActiveLearnDownloader
Pearson Active Learn Book Downloader

More information (not my video.)

https://www.youtube.com/watch?v=FVW6KuDQbhA

---

## Overview of How to Use

### You need:

1. The URL prefix and suffix of a page. (The part that comes before and after the page number in the URL)

  > https://resources.pearsonactivelearn.com/r00/r0021/r002163/r00216387/current/OPS/images/Access_Studio_Full_Book-
  
  > iterated number (001, 002, 003, 004... 201, 202, 203)
  
  Some iterated numbers have place holders before digits. No way to figure this out though. Also no way to figure out URL prefixes.

  > .pdf.jpg

2. The total number of pages in the book. This isn't neccessary, ~~but is relevant to prevent the downloader from running forever.~~ tasks now cancel after failing three times.

  > 32

3. Python 3.9 or above.

4. ~~The downloader script in a new empty folder.~~ Specify a folder name as the downloader now creates a folder to dump images into.

### To use it:

1. Edit the script in a text editor and edit the variables in FULL CAPS to your needs.

2. Re-run the python script, and all of the downloaded files will appear in the same folder the script is located in.

> **Note: If no files appear, it is because the script could not find the requested URL. Look at the python shell and check the links printed work fine in your browser.** The script will end after failing thrice consecutively.

---

## The Vulnerability

1. Sign into Active Learn and open the chosen book.

2. Right click the book and `Inspect` the page using chrome's devtools.

3. Change to the Sources tab and find the `index.html`

4. Open either the left or right page subdirectory `iframe` tags.

5. Open all subdirectories inside that iframe until you find an image.

6. EG: In the following image, the file is found in `https://resources.pearsonactivelearn.com/r00/r0021/r002139/r00213912/current/OPS/images/VIVA_SB_KS3_COMBINED_PDF_FOR_REFINERY-005.pdf.jpg`

![Screenshot of inspecting a book.](https://github.com/d1ddle/ActiveLearnDownloader/blob/main/instructions/instructions1.png)

7. Then you can right click the small image and open it in a new tab.

![Screenshot of opening in a new tab.](https://github.com/d1ddle/ActiveLearnDownloader/blob/main/instructions/instructions2.png?raw=true)

8. This link can be altered to give you access to the whole book without being signed in to Active Learn. We can do this by changing the page number at the end of the url and downloading the image!

9. So I wrote this quick python script to download all images from a book. You just need to give the script a maximum page number, filename url and off it goes.

10. Note: this also works with Kerboodle!

---

> **Note: filename url is the link to a page before the page number. EG: `https://resources.pearsonactivelearn.com/r00/r0021/r002163/r00216387/current/OPS/images/Access_Studio_Full_Book-` PAGENO `.pdf.jpg`**
> **Also note that the page number has to include 0 placeholders so that the total page number contains the same total number of digits as the page numbers. The downloader handles this**

---

## The Fix

Pearson Active Learn could use an encryption method using a private key to randomise the filenames used so that they can't be traced systematically using page numbers.

For example, page 1 would be called `T0JRV09aSlFHRT09PT09PQ==.jpg` which is Base32 and then Base64 encoded from page01, page 2 called `T0JRV09aSlFHST09PT09PQ==.jpg` which is Base32 and then Base64 encoded from page02, etc etc, using multiple different encoding and hashing types.

---

### Diclaimer

None of this was done to harm Pearson, Active Learn, Kerboodle or anyone, in fact, this is just a fun weekend project to look into their content delivery service.
