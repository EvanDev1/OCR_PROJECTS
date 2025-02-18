const fs = require('fs');

// Load the itemRecipes variable from item_recipes.js
const itemRecipes = require('./item_recipes');

// Function to convert duration to seconds
function convertDurationToSeconds(duration) {
    const { hr = 0, min = 0, sec = 0 } = duration;
    return hr * 3600 + min * 60 + sec;
}

// Iterate through each item's duration and convert to seconds
for (const item in itemRecipes) {
    if (itemRecipes.hasOwnProperty(item) && itemRecipes[item].duration) {
        itemRecipes[item].duration = convertDurationToSeconds(itemRecipes[item].duration);
    }
}

// Convert the updated JavaScript object to JavaScript code as a string
const jsCode = `const itemRecipes = ${JSON.stringify(itemRecipes, null, 4)};\n\nmodule.exports = itemRecipes;`;

// Write the updated JavaScript code to a new file
fs.writeFileSync('item_recipes_updated.js', jsCode);

console.log('JavaScript file with updated durations generated: item_recipes_updated.js');
