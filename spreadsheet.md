# Worked Example

There are so many different spreadsheet applications that we couldn't possibly provide guides for them all. So we've provided a worked example for how to get analysing using some free software called [Libre Office](https://www.libreoffice.org/) that's preinstalled on the Raspberry Pi operating system (Raspbian).

![](images/LibreOffice_logo.png)

## Raspbian

Before doing anything it's advisable to [download](https://www.raspberrypi.org/downloads/) the latest version of Raspbian *Jessie* and install it on your SD card. If you need help with this please read our [NOOBS setup guide](https://www.raspberrypi.org/help/noobs-setup/). Note that the video shows Raspbian *Wheezy* being installed, the Wheezy version is now out of date and does not come with Libre Office, Jessie does.

Boot up your Raspberry Pi as per usual using your new Raspbian Jessie SD card.

## Download the CSV zip file

Currently only the example data is available. This data was *not* recorded in space, it was captured at an office desk in in Cambridge. So please do not spend too much effort analysing it, it's only been provided so that you can examine the file layout and check that you can load it properly. The file you'll get from the ISS will use the same format and layout.

[Example CSV Download](https://github.com/raspberrypilearning/astro-pi-flight-data-analysis/blob/master/data/astro_pi_data_20150824_085954.zip?raw=true)

After downloading the zip file, open the *File Manager* application and navigate to the `Downloads` folder. The zip file should be shown on the right:

![](images/ex01.png)

Right click on the zip file and select `Extract Here` from the context menu.

![](images/ex02.png)

The CSV file containing the data should now appear.

## Load the CSV into Libre Office

Right click on the CSV file and select `LibreOffice Calc` from the context menu.

![](images/ex03.png)

The following dialogue will show. This allows you to configure how Libre Office Calc should import the data, the default options are fine so just click the OK button.

![](images/ex04.png)

The data will now show in the usual tabular spreadsheet layout.

## Copy data to work on

It is likely that the CSV file will contain upward of 30 thousand rows, possibly more depending on how long Tim Peake leaves the Astro Pis in flight recorder mode. This amount of data can cause Libre Office Calc to run *very slowly*. Especially when producing graphs (this will be very noticeable if you're using older models of the Raspberry Pi). So, for the purposes of this exercise, we're going to select the first 500 rows and copy them into a new spreadsheet to work on.

Start by clicking in the margin (where the red star is below) to select an entire row. Then hold down the shift key and use the cursor keys down arrow to select more rows.

![](images/ex05.png)

Keep going until you reach the 500th row.

![](images/ex06.png)

Then right click on the selected row (for instance where the red star is above) and select `Copy` from the context menu.

![](images/ex07.png)

Click on the green `+` symbol at the bottom of the program to create a new blank sheet.

![](images/ex08.png)

From the `Edit` menu at the top, select `Paste`

![](images/ex09.png)

The copied data should then appear.

![](images/ex10.png)

Working with only 500 rows will be a lot quicker and more responsive allowing you to get to grips with Libre Office Calc without having long processing delays between each step.

## Format the time stamp column

Currently the time stamp column is a *text* field. If you want to use in any calculations (for instance working out the time between two rows) then you'll need to format the entire column as *time* field. So let's do this now before we go any further.

Scroll to the right and find column `T` which should be `time_stamp`, right click on the column header and select `Format Cells` from the context menu.

![](images/ex11.png)

On the Numbers tab select `Time` under `Category` and then under `Format` choose the last option in the list that says `1999-12-31 13:37:46`

![](images/ex12.png)

Check that the format code is the same as in the picture above, then click OK.

## Plot humidity

We're going to make a graph of humidity versus time but feel free to use a different sensor if you prefer, the process is the same for all. Time will be on the horizontal X axis and the humidity measurement will be on the vertical Y axis. Scroll back to the left and find column `E` which should be `humidity`, left click on the column header (where the red star is below) to select all rows in the column.

![](images/ex13.png)

The Chart Wizard will now show. Under `Chart Type` select `Line` followed by `Lines Only`, now select step 3 (Data Series) from the left hand menu.

![](images/ex14.png)

Under `Data series` `humidity` should be selected, under `Data ranges` select `Y-Values`. You'll now see that the `Categories` box is empty. This box allows you to specify the corresponding horizontal X-axis values for the humidity on the Y-axis.

We saw from before that the time stamp data is in column `T` so enter the following to specify rows 2 to 500: `$Sheet2.$T$2:$T$500` and click Next.

![](images/ex15.png)

Step 4 (Chart Elements) just allows you to specify titles for the axes and for the graph itself, you can skip this if you want to.

![](images/ex16.png)

When you're ready click Finish.

## Examine the graph

You can expand the graph by clicking and dragging the resize zones on the edges and corners.

![](images/ex17.png)
