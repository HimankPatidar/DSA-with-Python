| Step                                   | Array State               |
|----------------------------------------|---------------------------|
| Initial                                | [1, 0, 2, 3, 0, 4, 5, 0] |
| Found 0 at index 1, shift right       | [1, 0, 0, 2, 3, 0, 4, 5] |
| Found 0 at index 4, shift right       | [1, 0, 0, 2, 3, 0, 0, 4] |
| Found 0 at index 7, shift right (Ignored last zero) | [1, 0, 0, 2, 3, 0, 0, 4] |
| Final Output                           | [1, 0, 0, 2, 3, 0, 0, 4] |
