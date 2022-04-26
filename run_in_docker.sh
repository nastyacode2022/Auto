
source ./env.sh

DATE_WITH_TIME=`date "+%Y%m%d_%H%M%S"`

set -x
docker run -it --rm \
-v $(pwd)/API_testing:/automation/api_testing \
-e WC_KEY=${WC_KEY} \
-e WC_SECRET=${WC_SECRET} \
-e DB_USER=${DB_USER} \
-e DB_PASSWORD=${DB_PASSWORD} \
api_test_06 \
pytest \
--html /automation/api_testing/results/my_results_${DATE_WITH_TIME}.html \
--color=yes \
-m "$1" /automation/api_testing
