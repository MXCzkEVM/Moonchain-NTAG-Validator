### Reset NTAG

This process only works for the NTAG initialized by the example code. It will not work for production code or other NTAGs.

1. Load the `test_ntag_dfu.zip` firmware.

2. Connect the Validator with minicom.

   ```
   minicom -b 115200 -8  -D /dev/ttyACM0 -o
   ```

3. Press the [ENTER] key and the menu will show up.

   ![x2e_test_ntag](/media/ian_lee/MxWorking2022/MatchX/iso/github_MXCzkEVM/Moonchain-NTAG-Validator/assets/x2e_test_ntag.png)

4. Place the validator to the NTAG and press [5] to reset the NTAG.

   ![x2e_reset_ntag](/media/ian_lee/MxWorking2022/MatchX/iso/github_MXCzkEVM/Moonchain-NTAG-Validator/assets/x2e_reset_ntag.png)

5. After done, press [0] and change the firmware back to `ntag_validator_dfu_ism2400.zip`.

