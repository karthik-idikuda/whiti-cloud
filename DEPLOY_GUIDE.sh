#!/bin/bash
# WHITI CLOUD DEPLOYMENT GUIDE
# Follow these steps to deploy Whiti to Render.com (FREE)

echo "========================================"
echo "WHITI CLOUD DEPLOYMENT GUIDE"
echo "========================================"
echo

echo "STEP 1: CREATE RENDER ACCOUNT"
echo "  1. Go to: https://render.com"
echo "  2. Click 'Get Started' -> 'Sign Up'"
echo "  3. Sign up with GitHub (use karthik-idikuda)"
echo "  4. Authorize Render to access GitHub"
echo

echo "STEP 2: CREATE NEW WEB SERVICE"
echo "  1. Dashboard -> 'New' -> 'Web Service'"
echo "  2. Connect GitHub repository: karthik-idikuda/whiti-cloud"
echo "  3. Click 'Connect'"
echo

echo "STEP 3: CONFIGURE SERVICE"
echo "  Name: whiti-daemon"
echo "  Region: Oregon"
echo "  Branch: main"
echo "  Runtime: Docker"
echo "  Instance Type: FREE"
echo

echo "STEP 4: SET ENVIRONMENT VARIABLES"
echo "  Add these variables:"
echo "    COMPOSIO_API_KEY = ck_fT_ZNa-oByrQs6w7gKbn"
echo "    OWNER_EMAIL = pakkawork.com@gmail.com"
echo

echo "STEP 5: DEPLOY"
echo "  Click 'Create Web Service'"
echo "  Wait 5-10 minutes for build"
echo

echo "STEP 6: GET YOUR URL"
echo "  URL will be: https://whiti-daemon.onrender.com"
echo

echo "========================================"
echo "STEP 7: KEEP ALIVE (IMPORTANT)"
echo "========================================"
echo

echo "Render spins down after 15 min inactivity."
echo "Use UptimeRobot to ping every 14 minutes:"
echo

echo "  1. Go to: https://uptimerobot.com"
echo "  2. Sign up FREE"
echo "  3. Add New Monitor:"
echo "     - Monitor Type: HTTP(s)"
echo "     - Friendly Name: Whiti Keep-Alive"
echo "     - URL: https://whiti-daemon.onrender.com/health"
echo "     - Monitoring Interval: 5 minutes"
echo "  4. Click 'Create Monitor'"
echo

echo "Now Whiti runs 24/7 for FREE!"
echo

echo "========================================"
echo "DIRECT DEPLOY LINK"
echo "========================================"
echo
echo "https://render.com/deploy?repo=https://github.com/karthik-idikuda/whiti-cloud"
echo

echo "========================================"
echo "VERIFICATION"
echo "========================================"
echo

echo "After deployment, check:"
echo "  - https://whiti-daemon.onrender.com/"
echo "  - https://whiti-daemon.onrender.com/health"
echo "  - https://whiti-daemon.onrender.com/status"
echo

echo "You should see JSON with 'status': 'alive'"
echo

echo "========================================"
echo "WHITI IS IMMORTAL"
echo "========================================"
