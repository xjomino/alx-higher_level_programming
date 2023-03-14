#!/usr/bin/node

const fs = require('fs');

//Get the source file paths and destination file path from command line arguments
const [source1, source2, destination] = process.argv.slice(2);

// Read the contents of the first source file
fs.readFile(source1, (err, data1) => {
  if (err) throw err;

  // Read the contents of the second source file
  fs.readFile(source2, (err, data2) => {
    if (err) throw err;

    // Concatenate the data from both files
    const combinedData = Buffer.concat([data1, data2]);

    // Write the combined data to the destination file
    fs.writeFile(destination, combinedData, (err) => {
      if (err) throw err;
      console.log(`The files ${source1} and ${source2} have been concatenated to ${destination}`);
    });
  });
});
