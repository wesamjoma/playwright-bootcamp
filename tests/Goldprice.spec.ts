import { test , expect } from '@playwright/test';

test('open gold price website' , async ({page}) => {
    await page.goto ('https://goldprice.org/');
});