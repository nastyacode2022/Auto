


docker run --rm -v /c/Users/ATarasova/PycharmProjects/Auto/API_testing:/automation/api_testing -e WC_KEY=ck_66def9128cb372bf9fd9ecf362eb142a7ed41026 -e WC_SECRET=cs_a488a05b34bc6fbfbe53b5b3397e8b823d4af330 -e DB_USER=root -e DB_PASSWORD=root api_test_06 pytest /automation/api_testing