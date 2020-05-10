# Estimation Project Writeup #

In this project, I developed the estimation portion of the controller used in the CPP simulator. I followed these steps:

### Step 1: Sensor Noise ###

I wrote a Python script to calculate the correct sensor noise standard deviations from recorded errors. 
These standard deviations were included in the config file `config/6_Sensornoise.txt` as `MeasuredStdDev_GPSPosXY` and `MeasuredStdDev_AccelXY`.
With these values, approx 68% of the respective measurements lie within +/- 1 sigma bound for a Gaussian noise model.

### Step 2: Attitude Estimation ###

In this step I included information from the IMU.  The goal was to improve the complementary filter-type attitude filter with a better rate gyro attitude integration scheme.
To this end, I changed the function `UpdateFromIMU()`. I used theQuaternion<float> class, which has a function for creating a quaternion from Euler angles. 


### Step 3: Prediction Step ###

This is the prediction step of the filter. I implemented the state prediction step in the `PredictState()` functon. Then I calculated the partial derivative of the body-to-global rotation matrix in the function `GetRbgPrime()`. Finally, I implemented the rest of the prediction step (predict the state covariance forward) in `Predict()`.
I also tunee the `QPosXYStd` and the `QVelXYStd` process parameters in `QuadEstimatorEKF.txt` such that the model captures the real error dynamics.


### Step 4: Magnetometer Update ###

Up until now we've only used the accelerometer and gyro for our state estimation.  In this step, I added the information from the magnetometer to improve the filter's performance in estimating the vehicle's heading. I also tuned the parameter `QYawStd` (`QuadEstimatorEKF.txt`) for the QuadEstimatorEKF so that it approximately captures the magnitude of the drift.


### Step 5: Closed Loop + GPS Update ###

In this step, I changed to use my own estimator instead of an ideal one by setting `Quad.UseIdealEstimator` to 0 in `config/11_GPSUpdate.txt`. I also changed from ideal to realistic IMU by changing the according lines in `config/11_GPSUpdate.txt`. Further, I adapted the process noise model in `QuadEstimatorEKF.txt` and implemented the EKF GPS Update in the function `UpdateFromGPS()`. The simulation now runs with an estimated position error of < 1m.

### Step 6: Adding Your Controller ###

Up to this point, we have been working with a controller that has been relaxed to work with an estimated state instead of a real state.  So now, I replaced `QuadController.cpp` with the controller I wrote in the last project, and I also changed to my `QuadControlParams.txt` from the last project. Finally, I did some more parameter tuning to stabilize the controller.