-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Mar 24, 2026 at 09:11 AM
-- Server version: 5.7.26
-- PHP Version: 7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nutrifit_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `appointment_tb`
--

DROP TABLE IF EXISTS `appointment_tb`;
CREATE TABLE IF NOT EXISTS `appointment_tb` (
  `a_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` int(11) NOT NULL,
  `n_id` int(11) NOT NULL,
  `s_id` int(11) NOT NULL,
  `a_title` varchar(100) NOT NULL,
  `a_symptoms` text NOT NULL,
  `a_date` date NOT NULL,
  `a_fees` double NOT NULL,
  `a_remarks` text NOT NULL,
  `a_status` enum('Pending','Approved','Cancel') NOT NULL,
  `a_cdate` datetime NOT NULL,
  `a_udate` datetime NOT NULL,
  PRIMARY KEY (`a_id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `appointment_tb`
--

INSERT INTO `appointment_tb` (`a_id`, `u_id`, `n_id`, `s_id`, `a_title`, `a_symptoms`, `a_date`, `a_fees`, `a_remarks`, `a_status`, `a_cdate`, `a_udate`) VALUES
(1, 2, 16, 6, 'Fat Loss Guidance', 'Weight is stuck despite dieting.', '2026-01-11', 1000, 'Meal timing and lifestyle changes advised.', 'Pending', '2026-01-10 21:17:54', '2026-01-10 21:17:54'),
(2, 2, 14, 7, 'Asthma', 'Difficulty in breathing.', '2026-01-13', 1500, 'Immunity-support nutrition advised.', 'Pending', '2026-01-10 21:19:50', '2026-01-10 21:19:50'),
(3, 2, 9, 4, 'Fungal Infections', 'Burning sensation', '2026-01-14', 1500, 'Recurrent fungal infection suspected.', 'Approved', '2026-01-10 21:25:12', '2026-01-10 21:25:12'),
(4, 6, 14, 7, 'Wheezing', 'Wheezing sound while breathing.', '2026-01-16', 1500, 'Patient presents with wheezing suggestive of airway obstruction. Further evaluation and treatment advised.', 'Pending', '2026-01-10 21:28:59', '2026-01-10 21:28:59'),
(5, 6, 6, 3, 'Kidney Stones', 'Pain during urination', '2026-01-16', 1500, 'Symptoms suggestive of renal calculi (kidney stones). Further evaluation and management advised.', 'Approved', '2026-01-10 21:31:44', '2026-01-10 21:31:44'),
(6, 6, 15, 8, 'Muscle Gain', 'Muscle cramps', '2026-01-18', 1000, 'Pre- and post-workout nutrition discussed.', 'Pending', '2026-01-10 21:33:22', '2026-01-10 21:33:22'),
(18, 3, 2, 5, 'Hight Growth Issue', 'Height significantly lower than peers of the same age.', '2026-02-07', 1500, 'remarks', 'Cancel', '2026-01-31 14:02:47', '2026-01-31 14:02:47'),
(8, 3, 8, 2, 'PCOS/PCODproblem', 'Irregular Periods', '2026-01-20', 2000, 'Follow-up for cycle regulation recommended.', 'Pending', '2026-01-10 21:36:38', '2026-01-10 21:36:38'),
(9, 3, 4, 3, 'Wheezing', 'Respiratory consultation & evaluation.', '2026-01-21', 1500, 'Recurrent wheezing observed. Diet modifications and further evaluation advised.', 'Approved', '2026-01-10 21:39:50', '2026-01-10 21:39:50'),
(10, 4, 11, 6, 'Underweight', 'Weak immune system', '2026-01-21', 1500, 'Recovery nutrition plan advised.', 'Approved', '2026-01-10 21:42:38', '2026-01-10 21:42:38'),
(11, 4, 1, 1, 'Thyroid Diet Consultation', 'Diagnosed with thyroid disorder.', '2026-01-23', 1000, 'Thyroid-friendly balanced diet recommended.', 'Approved', '2026-01-10 21:44:05', '2026-01-10 21:44:05'),
(12, 4, 7, 4, 'Skin Problems', 'Dry, flaky, or scaly skin.', '2026-01-19', 2000, 'Chronic skin condition observed. Management and follow-up advised.', 'Approved', '2026-01-10 21:47:20', '2026-01-10 21:47:20'),
(13, 5, 3, 1, 'Hormonal Imbalance', 'High blood sugar', '2026-01-20', 1000, 'Seeking personalized diet plan for weight and hormonal balance.', 'Approved', '2026-01-10 21:59:12', '2026-01-10 21:59:12'),
(14, 5, 12, 8, 'Body Composition', 'Endurance improvement.', '2026-01-17', 1500, 'Interested in personalized meal & supplement plan.', 'Approved', '2026-01-10 22:03:01', '2026-01-10 22:03:01'),
(15, 5, 13, 5, 'Growth & Development Assessment', 'Stomach pain and diarrhea.', '2026-01-30', 2000, 'Any allergies or chronic conditions.', 'Approved', '2026-01-10 22:06:12', '2026-01-10 22:06:12'),
(16, 1, 5, 2, 'PCOD problem', 'Hormonal Imbalance.', '2026-01-23', 1000, 'Looking for treatment and diet/lifestyle guidance.', 'Approved', '2026-01-10 22:12:09', '2026-01-10 22:12:09'),
(17, 1, 16, 6, 'Fat Loss Guidance', 'Weight is stuck despite dieting.', '2026-01-31', 1000, 'Meal timing and lifestyle changes advised.', 'Approved', '2026-01-10 22:13:57', '2026-01-10 22:13:57'),
(20, 3, 11, 6, 'Fat Loss Guidance', 'Weight is stuck despite dieting.', '2026-03-14', 1500, 'Meal timing and lifestyle changes advised.', 'Approved', '2026-03-12 10:16:33', '2026-03-12 10:16:33'),
(21, 6, 11, 6, 'Muscle Gain', 'Muscles Cramps.', '2026-03-13', 1500, 'Pre- and post-workout nutrition discussed.', 'Cancel', '2026-03-12 10:22:27', '2026-03-12 10:22:27');

-- --------------------------------------------------------

--
-- Table structure for table `consult_tb`
--

DROP TABLE IF EXISTS `consult_tb`;
CREATE TABLE IF NOT EXISTS `consult_tb` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `a_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL,
  `n_id` int(11) NOT NULL,
  `c_title` varchar(100) NOT NULL,
  `c_treatment` text NOT NULL,
  `c_file` varchar(100) NOT NULL,
  `c_fees` double NOT NULL,
  `c_date` date NOT NULL,
  `c_cdate` datetime NOT NULL,
  `c_udate` datetime NOT NULL,
  PRIMARY KEY (`c_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `consult_tb`
--

INSERT INTO `consult_tb` (`c_id`, `a_id`, `u_id`, `n_id`, `c_title`, `c_treatment`, `c_file`, `c_fees`, `c_date`, `c_cdate`, `c_udate`) VALUES
(1, 11, 4, 1, 'Thyroid Diet Consultation', 'Thyroid Diet Consultation', 'Thyroid_Diet.pdf', 2000, '2026-01-30', '2026-01-10 22:20:42', '2026-01-10 22:20:42'),
(2, 7, 3, 2, 'Diet Plan', 'Protein Sources\r\nEggs, milk, yogurt, cheese\r\nLean meats: chicken, fish\r\nLentils, beans, chickpeas.', 'Child_Diet_3jm0XUV.pdf', 2500, '2026-02-01', '2026-01-10 22:24:19', '2026-01-10 22:24:19'),
(3, 13, 5, 3, 'Hormonal Imbalance', 'Evaluation of symptoms (weight gain, fatigue, irregular periods, hair fall, acne, mood swings)', 'PCOD_DYHQzGq.pdf', 1700, '2026-01-16', '2026-01-11 22:08:35', '2026-01-11 22:08:35'),
(4, 5, 6, 6, 'Kidney Stones Management Consultation', 'Identification of stone type (calcium oxalate, uric acid, cystine, struvite)', 'Kidney_Stone_9vf1r7n.pdf', 1550, '2026-01-14', '2026-01-11 22:12:40', '2026-01-11 22:12:40'),
(5, 3, 2, 9, 'Fungal Infection Recovery & Prevention Consult', 'Identification of the type of fungal infection (skin, nail, scalp, intimate area)', 'Skin_Problem_6SRoFu8.pdf', 1370, '2026-01-14', '2026-01-11 22:17:22', '2026-01-11 22:17:22'),
(6, 10, 4, 11, 'Underweight Management Consultation &', 'Achieve healthy and sustainable weight gain', 'Fat_Loss_GIdstuK.pdf', 1420, '2026-01-26', '2026-01-11 22:23:14', '2026-01-11 22:23:14'),
(7, 14, 5, 12, 'Body Composition Analysis', 'Detailed body composition assessment (fat %, muscle mass, water %, BMI)\r\nEvaluation of lifestyle, diet, and activity level', 'Fat_Loss_PqtKKrU.pdf', 1610, '2026-01-21', '2026-01-11 22:25:21', '2026-01-11 22:25:21'),
(10, 2, 2, 14, 'Asthma Management & Care Consultation', 'Comprehensive medical and symptom assessment\r\nEvaluation of triggers (allergens, dust, pollution, diet, stress)\r\nPersonalized nutrition plan to support lung health and immunity\r\nAnti-inflammatory and antioxidant-rich diet recommendations', 'Kidney_Stone_DbTwoKB.pdf', 1840, '2026-01-21', '2026-01-11 22:30:53', '2026-01-11 22:30:53'),
(11, 17, 1, 16, 'Fat Loss Guidance', 'Detailed body composition and health assessment\r\nEvaluation of lifestyle, diet, and activity patterns\r\nPersonalized fat-loss nutrition plan\r\nCalorie management and macronutrient balance', 'Fat_Loss_dxBNw3R.pdf', 1800, '2026-01-15', '2026-01-11 22:33:25', '2026-01-11 22:33:25'),
(12, 5, 6, 6, 'Kedney Stone Treatment', 'Depends on stone type, but generally:\r\nDrink enough water to keep urine pale\r\nReduce salt\r\nModerate animal protein\r\nDon’t overdo calcium supplements (food calcium is usually fine)', 'Kidney_Stone_DLwWujx.pdf', 2500, '2026-02-14', '2026-02-02 20:52:44', '2026-02-02 20:52:44'),
(13, 10, 4, 11, 'Underweight', 'Underweight Treatment – Diet Consultation.', 'Muscle_Gain_TcSnIjJ.pdf', 2000, '2026-02-15', '2026-03-11 23:45:17', '2026-03-11 23:45:17');

-- --------------------------------------------------------

--
-- Table structure for table `feedback_tb`
--

DROP TABLE IF EXISTS `feedback_tb`;
CREATE TABLE IF NOT EXISTS `feedback_tb` (
  `f_id` int(11) NOT NULL AUTO_INCREMENT,
  `f_name` varchar(20) NOT NULL,
  `f_contact` bigint(20) NOT NULL,
  `f_message` text NOT NULL,
  `f_status` enum('Show','Hide') NOT NULL,
  `f_cdate` datetime NOT NULL,
  `f_udate` datetime NOT NULL,
  PRIMARY KEY (`f_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feedback_tb`
--

INSERT INTO `feedback_tb` (`f_id`, `f_name`, `f_contact`, `f_message`, `f_status`, `f_cdate`, `f_udate`) VALUES
(1, 'Navneet Kaur', 9991935129, 'I’ve been following NutriFit’s nutrition and workout plans for a few months now, and the results are incredible. I feel more energetic, my stamina has improved, and I’m finally achieving my fitness goals. The plans are easy to follow and really motivating. Highly recommend it to anyone serious about health. Thank You !', 'Show', '2025-12-31 12:00:37', '2025-12-31 12:04:00'),
(2, 'Urvashi Chavada', 9016303552, 'NutriFit has changed the way I approach my health. The personalized nutrition guidance and workout plans are practical and effective. I’ve lost weight in a healthy way and feel stronger every day. It’s amazing how something so simple can make such a big difference!', 'Show', '2025-12-31 12:01:32', '2025-12-31 12:03:58'),
(3, 'Palak Raval', 8799271334, 'Following NutriFit has been a game-changer for me. The program is easy to stick to, and I’ve seen real improvements in my energy and fitness. I love how it fits into my lifestyle without being overwhelming. Truly a fantastic resource for anyone wanting to get healthier!', 'Show', '2025-12-31 12:02:00', '2025-12-31 12:03:55'),
(4, 'Shivam Patel', 7600682624, 'I was struggling with energy and consistency in my workouts before NutriFit. Now, I feel motivated, energized, and confident about my fitness journey. The meal plans are practical, and the exercises are effective. NutriFit makes achieving a healthy lifestyle simple and enjoyable!', 'Show', '2025-12-31 12:02:37', '2025-12-31 12:03:52'),
(5, 'Pratik Raval', 7096996399, 'Thanks to NutriFit, I’ve finally managed to balance my busy schedule with fitness. The meal and exercise plans are realistic and effective. I feel lighter, energized, and more focused. It’s truly a holistic approach to wellness.!', 'Show', '2025-12-31 12:03:28', '2025-12-31 12:03:47');

-- --------------------------------------------------------

--
-- Table structure for table `login_tb`
--

DROP TABLE IF EXISTS `login_tb`;
CREATE TABLE IF NOT EXISTS `login_tb` (
  `l_id` int(11) NOT NULL AUTO_INCREMENT,
  `l_username` varchar(20) NOT NULL,
  `l_password` varchar(10) NOT NULL,
  `l_image` varchar(100) NOT NULL,
  `l_lastseen` datetime NOT NULL,
  PRIMARY KEY (`l_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login_tb`
--

INSERT INTO `login_tb` (`l_id`, `l_username`, `l_password`, `l_image`, `l_lastseen`) VALUES
(1, 'Priya', '12345', 'mahi.jpg', '2025-12-01 19:26:59'),
(2, 'Navneet', '12345', 'nav.jpg', '2026-03-11 22:37:06'),
(3, 'Palak', '12345', 'paluu.jpg', '2026-03-21 15:31:20'),
(4, 'Urvashi', '12345', 'urvi.jpg', '2026-03-24 14:23:38'),
(5, 'Snehal', '12345', 'snehal.jpg', '2025-11-26 23:35:44');

-- --------------------------------------------------------

--
-- Table structure for table `nutritionist_tb`
--

DROP TABLE IF EXISTS `nutritionist_tb`;
CREATE TABLE IF NOT EXISTS `nutritionist_tb` (
  `n_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_id` int(11) NOT NULL,
  `n_name` varchar(20) NOT NULL,
  `n_contact` bigint(20) NOT NULL,
  `n_address` text NOT NULL,
  `n_gender` enum('Male','Female') NOT NULL,
  `n_image` varchar(100) NOT NULL,
  `n_experience` text NOT NULL,
  `n_certificate` varchar(100) NOT NULL,
  `n_fees` double NOT NULL,
  `n_password` varchar(20) NOT NULL,
  `n_status` enum('Active','Deactive') NOT NULL,
  `n_cdate` datetime NOT NULL,
  `n_udate` datetime NOT NULL,
  PRIMARY KEY (`n_id`)
) ENGINE=MyISAM AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `nutritionist_tb`
--

INSERT INTO `nutritionist_tb` (`n_id`, `s_id`, `n_name`, `n_contact`, `n_address`, `n_gender`, `n_image`, `n_experience`, `n_certificate`, `n_fees`, `n_password`, `n_status`, `n_cdate`, `n_udate`) VALUES
(1, 1, 'Dr. Yuvraj Mehta', 8469430029, 'Survey No 148, Plot No 154/2, opp. PRAMUKH HARMONY, Sargasan, Gandhinagar, Gujarat 382419', 'Male', 'n9.jpg', 'I am a qualified Endocrinologist with over 10 years of professional experience in diagnosing and managing hormonal and metabolic disorders. I specialize in diabetes, thyroid disorders, adrenal and pituitary gland conditions, and metabolic syndrome. I provide comprehensive care for both adults and children with endocrine disorders. I design individualized treatment plans that integrate medication, lifestyle modifications, and nutrition guidance. I closely monitor patient progress and adjust therapies to achieve optimal outcomes. I educate patients on self-management, disease prevention, and healthy lifestyle practices. \r\nI work collaboratively with multidisciplinary healthcare teams to ensure holistic patient care. I emphasize evidence-based, patient-centered approaches in all treatments. My goal is to help patients achieve hormonal balance, improve metabolism, and enhance overall well-being.', 'certi1.png', 1000, '12345', 'Active', '2025-11-27 00:00:00', '2026-01-10 22:22:33'),
(2, 5, 'Dr. Mahek Shah', 9016303553, 'SWAGAT RAINFOREST-1, D12, Kudasan-Por Rd, near HDFC Bank and black Papper Hotel, Kudasan, Gandhinagar, Gujarat 382419', 'Female', 'n1.jpg', 'I am a qualified Pediatrician with over 10 years of professional experience in child healthcare. I provide comprehensive care for infants, children, and adolescents, focusing on growth, development, and preventive health. I manage common and complex pediatric conditions, including infections, asthma, allergies, nutrition-related issues, and chronic illnesses. I monitor growth and development using standardized growth charts and developmental milestones. I provide vaccination counseling and ensure timely immunizations. \r\nI offer guidance to parents and caregivers on nutrition, hygiene, and healthy lifestyle practices. I work closely with multidisciplinary teams to ensure holistic care for each child. I emphasize patient-centered, compassionate, and evidence-based approaches. My goal is to promote healthy growth, prevent illness, and support the overall well-being of children at every stage of development.', 'certi2.png', 1500, '12345', 'Active', '2025-11-19 00:00:00', '2026-01-31 14:21:35'),
(3, 1, 'Dr. Mahi Prajapati', 8799076590, 'Sahaj Icon, 401-404, Anand Mahal Rd, near Prime Arcade, Honey Park, Adajan Gam, Adajan, Surat, Gujarat 395009', 'Female', 'n3.jpg', 'I am a qualified Endocrinologist with over 10 years of professional experience in diagnosing and managing hormonal and metabolic disorders. I specialize in diabetes, thyroid disorders, adrenal and pituitary gland conditions, and metabolic syndrome. I provide comprehensive care for both adults and children with endocrine disorders. I design individualized treatment plans that combine medication, lifestyle modifications, and nutrition guidance. I closely monitor patient progress and adjust therapies to achieve optimal health outcomes. I educate patients on self-management, disease prevention, and healthy lifestyle practices. I collaborate with multidisciplinary healthcare teams to ensure holistic patient care. I emphasize evidence-based, patient-centered approaches in all treatments. My goal is to help patients achieve hormonal balance, improved metabolism, and overall well-being.', 'certi3.png', 1000, '12345', 'Active', '2025-11-10 08:11:59', '2026-01-11 22:08:50'),
(4, 3, 'Dr. Surabhi Patel', 8555887098, 'D/1 shaktikrupa soc, Subhanpura, opp. Arunachal Society, Vadodara, Gujarat 390023', 'Male', 'n4.jpg', 'I am a qualified Dietitian with over 10 years of professional experience in nutrition and lifestyle management. I provide personalized nutrition care for individuals of all age groups. I specialize in weight management and therapeutic diets for lifestyle-related disorders. I design customized meal plans for conditions such as diabetes, PCOS, thyroid disorders, hypertension, and digestive issues. I focus on practical, balanced, and sustainable eating habits. I provide nutrition counseling for pregnancy, lactation, and child nutrition. I follow evidence-based nutrition practices and emphasize long-term lifestyle changes. I work closely with doctors and healthcare professionals to support holistic patient care. I educate clients on portion control, mindful eating, and healthy habits. My goal is to improve overall health, energy levels, and quality of life through proper nutrition. I am passionate about helping clients achieve their health goals and promoting lifelong wellness.', 'certi4.png', 1500, '12345', 'Active', '2025-11-01 14:13:30', '2026-01-09 14:41:14'),
(5, 2, 'Dr. Pratik Joshi', 6790865432, 'phase 2, prince Villa, 156, Gotri - Sevasi Rd, behind Collabera, Chandramauleshwar Nagar, Gotri, Vadodara, Gujarat 390021', 'Male', 'n10.jpg', 'I am a Dermatologist with over 12 years of experience in diagnosing and treating skin, hair, and nail conditions. I specialize in acne, eczema, psoriasis, pigmentation disorders, fungal and bacterial infections. I provide advanced care for hair loss, dandruff, alopecia, and scalp disorders. I offer medical and cosmetic dermatology services, including chemical peels, acne scar management, and anti-aging treatments. I focus on personalized, evidence-based treatment plans tailored to each patient’s skin type. I emphasize patient education, skincare routines, and long-term skin health. I follow strict safety and hygiene protocols in all procedures. My goal is to restore healthy skin, boost confidence, and ensure patient satisfaction.', 'certi5.png', 1000, '12345', 'Active', '2025-09-04 06:11:29', '2026-01-11 22:09:56'),
(6, 3, 'Dr. Krisha Joshi', 7600682624, 'Tilak Nagar Society, 8, Goddan Park Rd, opp. Welcome Hotel, Sardar Colony, Ahmedabad, Gujarat 380013', 'Female', 'n5.jpg', 'I am a qualified Dietitian with over 10 years of professional experience in nutrition and lifestyle management. I provide personalized nutrition care for individuals across all age groups. I specialize in weight management and therapeutic diets for lifestyle disorders. I design customized meal plans for conditions such as diabetes, PCOS, thyroid disorders, hypertension, and digestive problems. I focus on practical, balanced, and sustainable eating habits. I provide nutrition counseling for pregnancy, lactation, and child nutrition. I follow evidence-based nutrition practices. I work closely with doctors and healthcare professionals to support holistic patient care. I educate clients on portion control, mindful eating, and long-term lifestyle changes. My goal is to improve overall health, energy levels, and quality of life through proper nutrition.', 'certi6.png', 1500, '12345', 'Active', '2025-12-23 00:32:46', '2026-03-24 14:24:24'),
(7, 4, 'Dr. Ronak Sharma', 7016664771, 'Block No 21, Poliece Line, opp. Divajipura, Dariakhan Ghummat, Government A Colony, Shahibag, Ahmedabad, Gujarat 380004', 'Female', 'n7.jpg', 'I am a Gynaecologist with over 10 years of professional experience in women’s healthcare. I specialize in managing menstrual disorders, PCOS, infertility, and hormonal imbalances. I provide comprehensive antenatal, postnatal, and high-risk pregnancy care. I have expertise in family planning, contraception counseling, and menopause management. I manage gynecological infections, fibroids, ovarian cysts, and endometriosis. I perform routine gynecological examinations, screenings, and preventive care. I focus on patient-centered, ethical, and evidence-based treatment approaches. I ensure compassionate care, privacy, and clear communication with every patient. My goal is to support women’s health, safety, and overall well-being at every stage of life.', 'certi7.png', 2000, '12345', 'Active', '2025-12-26 11:28:45', '2026-01-10 22:29:06'),
(8, 2, 'Dr. Karan Randhawa', 9991935342, '5 th Floor Body care Complex Opposite Wadaj Bus Stand Ashram Road, \r\nDandi Kuch Cir, \r\nAhmedabad,\r\nGujarat 380013', 'Male', 'n11.jpg', 'I am a Dermatologist with over 12 years of experience in diagnosing and treating skin, hair, and nail conditions. I specialize in acne, eczema, psoriasis, pigmentation disorders, fungal and bacterial infections. I provide advanced care for hair loss, dandruff, alopecia, and scalp disorders. I offer medical and cosmetic dermatology services, including chemical peels, acne scar management, and anti-aging treatments. I focus on personalized, evidence-based treatment plans tailored to each patient’s skin type. I emphasize patient education, skincare routines, and long-term skin health. I follow strict safety and hygiene protocols in all procedures. My goal is to restore healthy skin, boost confidence, and ensure patient satisfaction.', 'certi8.png', 2000, '12345', 'Active', '2025-12-29 14:34:33', '2026-01-11 22:18:21'),
(9, 4, 'Dr. Anand Nair', 7041161501, '8, Green Villa Complex, Near HB Kapadiya School Road, Gurukul Rd, Memnagar, Ahmedabad, Gujarat 380052', 'Male', 'n13.jpg', 'I am a qualified Gynaecologist with over 10 years of professional experience in women’s healthcare. I specialize in managing menstrual disorders, PCOS, infertility, and hormonal imbalances. I provide comprehensive antenatal, postnatal, and high-risk pregnancy care. I have expertise in family planning, contraception counseling, and menopause management. I manage gynecological infections, fibroids, ovarian cysts, and endometriosis. I perform routine gynecological examinations, screenings, and preventive care. I focus on patient-centered, ethical, and evidence-based treatment approaches. I ensure compassionate care, privacy, and clear communication with every patient. My goal is to support women’s health, safety, and overall well-being at every stage of life.', 'certi9.png', 1500, '12345', 'Active', '2025-12-29 22:58:18', '2026-01-11 22:17:32'),
(10, 7, 'Dr Komal Patel', 9723001502, '302, 3rd Floor, Gandhinagar-382022', 'Male', 'n14.jpg', 'I am a qualified Pulmonologist with over 10 years of professional experience in diagnosing and treating respiratory and lung-related conditions. I provide comprehensive care for patients with asthma, chronic obstructive pulmonary disease (COPD), pneumonia, tuberculosis, and other lung disorders, ensuring accurate diagnosis and effective treatment plans.\r\n\r\nI specialize in managing both acute and chronic respiratory conditions, using evidence-based approaches to improve lung function, relieve symptoms, and prevent complications. I also provide guidance on lifestyle changes, smoking cessation, and preventive care to maintain long-term respiratory health.\r\n\r\nI work closely with multidisciplinary teams, including critical care specialists, physiotherapists, and nutritionists, to provide holistic care. My approach is patient-centered, compassionate, and tailored to each individual’s needs, focusing on improving quality of life and overall wellness.\r\n\r\nWith a decade of hands-on experience, I am committed to empowering patients to take control of their respiratory health, manage chronic conditions effectively, and lead active, healthy lives. My goal is to provide high-quality care, early intervention, and ongoing support for every patient’s lung and breathing health.', 'certi10.png', 1000, '12345', 'Active', '2025-12-30 10:12:36', '2026-01-09 14:20:42'),
(11, 6, 'Dr. Urvashi Chavada', 9016303552, '38, Green Villa Complex, Near HB Kapadiya School Road, Gurukul Rd, Memnagar, Ahmedabad, Gujarat 380052', 'Female', 'n2.jpg', 'I am a qualified Nephrologist with over 15 years of professional experience in diagnosing and managing kidney and urinary system disorders. I specialize in chronic kidney disease, acute kidney injury, electrolyte and fluid imbalances, and renal replacement therapies, including dialysis. I provide comprehensive care for both adults and children with kidney-related conditions. I design individualized treatment plans that integrate medication, dietary guidance, and lifestyle modifications. I closely monitor patient progress and adjust therapies to achieve optimal renal outcomes. I educate patients on kidney health, disease prevention, and self-management strategies. I work collaboratively with multidisciplinary healthcare teams to ensure holistic patient care. I emphasize evidence-based, patient-centered approaches in all treatments. My goal is to help patients preserve kidney function, manage complications, and improve overall quality of life.', 'certi11.png', 1500, '12345', 'Active', '2025-12-30 21:50:33', '2026-03-12 10:38:38'),
(12, 8, 'Dr. Priya Sharma', 7600682625, 'Shalin Complex, Rd No. 5, Sector 22, Gandhinagar, Gujarat 382021', 'Female', 'n6.jpg', 'I am a qualified Sports Nutritionist with over 10 years of professional experience helping athletes, fitness enthusiasts, and active individuals optimize their performance through proper nutrition. I provide personalized nutrition plans tailored to individual energy requirements, training schedules, and fitness goals to enhance performance and recovery.\r\n\r\nI specialize in nutrition for endurance, strength, and team sports, as well as managing weight, muscle gain, and overall health optimization. My approach emphasizes evidence-based strategies, proper macronutrient balance, hydration, and supplementation to support peak athletic performance.\r\n\r\nI work closely with coaches, trainers, and healthcare professionals to create holistic plans that integrate nutrition with training and recovery strategies. I also educate clients on meal timing, pre- and post-workout nutrition, and lifestyle habits that support long-term fitness and well-being.\r\n\r\nWith a decade of hands-on experience, I am committed to empowering athletes and active individuals to achieve their full potential, prevent injuries, and maintain sustainable results through smart, science-backed nutrition guidance.', 'certi12.png', 1500, '12345', 'Active', '2025-11-11 00:00:00', '2026-01-31 11:41:15'),
(13, 5, 'Dr. Jaimin Gaurav', 9991935344, 'prince Villa, 156, Gotri - Sevasi Rd, behind Collabera, Chandramauleshwar Nagar, Gotri, Vadodara, Gujarat 390021', 'Male', 'n15.jpg', 'I am a qualified Pediatrician with over 10 years of professional experience in child healthcare. I provide comprehensive care for infants, children, and adolescents, focusing on growth, development, and preventive health. My goal is to ensure every child receives personalized, compassionate care that supports their physical and emotional well-being.\r\n\r\nI manage both common and complex pediatric conditions, including infections, asthma, allergies, nutrition-related issues, and chronic illnesses. I closely monitor growth and development using standardized growth charts and developmental milestones to identify any concerns early.\r\n\r\nI provide guidance to parents and caregivers on nutrition, hygiene, vaccination schedules, and healthy lifestyle practices. I work collaboratively with multidisciplinary teams to deliver holistic, evidence-based care tailored to each child’s needs.\r\n\r\nWith over a decade of hands-on experience, I am dedicated to promoting healthy growth, preventing illness, and supporting the overall well-being of children. My approach combines clinical expertise, practical strategies, and compassionate care to ensure children thrive at every stage of development.', 'certi13.png', 2000, '12345', 'Active', '2025-12-29 14:34:33', '2026-01-12 09:30:30'),
(14, 7, 'Dr. Jasvant Kapdiya', 7041168402, 'Windward Business Park, Aadicura Superspeciality Hospital, Jetalpur Rd, Anand Nagar, Haripura, Vadodara, Gujarat 390007', 'Male', 'n16.jpg', 'I am a qualified Pulmonologist with over 10 years of professional experience in diagnosing and treating respiratory and lung-related conditions. I provide comprehensive care for patients with asthma, chronic obstructive pulmonary disease (COPD), pneumonia, tuberculosis, and other lung disorders, ensuring accurate diagnosis and effective treatment plans.\r\n\r\nI specialize in managing both acute and chronic respiratory conditions, using evidence-based approaches to improve lung function, relieve symptoms, and prevent complications. I also provide guidance on lifestyle changes, smoking cessation, and preventive care to maintain long-term respiratory health.\r\n\r\nI work closely with multidisciplinary teams, including critical care specialists, physiotherapists, and nutritionists, to provide holistic care. My approach is patient-centered, compassionate, and tailored to each individual’s needs, focusing on improving quality of life and overall wellness.\r\n\r\nWith a decade of hands-on experience, I am committed to empowering patients to take control of their respiratory health, manage chronic conditions effectively, and lead active, healthy lives. My goal is to provide high-quality care, early intervention, and ongoing support for every patient’s lung and breathing health.', 'certi14.png', 1500, '12345', 'Active', '2025-12-23 00:32:46', '2026-01-11 22:32:03'),
(15, 8, 'Dr.Mohammad Farooque', 9016303550, 'Smera Square, Harmony Multispeciality Hospital, Tran Rasta, nr. Ayurvedic, Panigate, Relief Colony, Yakutpura, Vadodara, Gujarat 390019', 'Male', 'n12.jpg', 'I am a qualified Sports Nutritionist with over 10 years of professional experience helping athletes, fitness enthusiasts, and active individuals optimize their performance through proper nutrition. I provide personalized nutrition plans tailored to individual energy requirements, training schedules, and fitness goals to enhance performance and recovery.\r\n\r\nI specialize in nutrition for endurance, strength, and team sports, as well as managing weight, muscle gain, and overall health optimization. My approach emphasizes evidence-based strategies, proper macronutrient balance, hydration, and supplementation to support peak athletic performance.\r\n\r\nI work closely with coaches, trainers, and healthcare professionals to create holistic plans that integrate nutrition with training and recovery strategies. I also educate clients on meal timing, pre- and post-workout nutrition, and lifestyle habits that support long-term fitness and well-being.\r\n\r\nWith a decade of hands-on experience, I am committed to empowering athletes and active individuals to achieve their full potential, prevent injuries, and maintain sustainable results through smart, science-backed nutrition guidance.', 'certi15.png', 1000, '12345', 'Active', '2025-11-19 00:00:00', '2026-01-09 14:40:18'),
(16, 6, 'Dr. Ruchi Joshi', 9726503705, '303, 3rd floor, Golden Icon, Bird circle, Race Course Rd, Alkapuri, Vadodara, Gujarat 390007', 'Female', 'n8.jpg', 'I am a qualified Nephrologist with over 10 years of professional experience in diagnosing and managing kidney-related conditions. I provide comprehensive care for patients with chronic kidney disease, acute kidney injuries, hypertension-related kidney issues, and electrolyte imbalances, ensuring effective treatment and long-term kidney health.\r\n\r\nI specialize in both common and complex kidney disorders, offering evidence-based approaches for prevention, treatment, and management. I closely monitor key indicators such as glomerular filtration rate (GFR), creatinine, and electrolyte levels to track kidney function and adjust treatment plans accordingly.\r\n\r\nI work collaboratively with multidisciplinary teams, including dietitians, endocrinologists, and primary care physicians, to provide holistic care that addresses both kidney health and overall well-being. I also educate patients on lifestyle modifications, diet, and preventive strategies to protect kidney function.\r\n\r\nWith a decade of hands-on experience, I am committed to empowering patients to manage kidney disease effectively, prevent complications, and maintain a healthy, active life. My goal is to provide compassionate, evidence-based care that supports long-term kidney health and enhances quality of life.', 'certi16.png', 1000, '12345', 'Active', '2025-12-23 00:32:46', '2026-01-31 14:47:56');

-- --------------------------------------------------------

--
-- Table structure for table `payment_tb`
--

DROP TABLE IF EXISTS `payment_tb`;
CREATE TABLE IF NOT EXISTS `payment_tb` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_id` int(11) NOT NULL,
  `n_id` int(11) NOT NULL,
  `p_type` enum('Appointment','Consult') NOT NULL,
  `p_payment_id` int(11) NOT NULL,
  `p_amount` double NOT NULL,
  `p_status` enum('Success','Failed') NOT NULL,
  `p_cdate` datetime NOT NULL,
  `p_udate` datetime NOT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=MyISAM AUTO_INCREMENT=42 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `payment_tb`
--

INSERT INTO `payment_tb` (`p_id`, `u_id`, `n_id`, `p_type`, `p_payment_id`, `p_amount`, `p_status`, `p_cdate`, `p_udate`) VALUES
(1, 2, 16, 'Appointment', 1, 1000, 'Success', '2026-01-10 21:18:18', '2026-01-10 22:21:57'),
(2, 2, 14, 'Appointment', 2, 1500, 'Success', '2026-01-10 21:20:13', '2026-01-10 21:20:13'),
(3, 2, 9, 'Appointment', 3, 1500, 'Success', '2026-01-10 21:25:33', '2026-01-10 21:25:33'),
(4, 6, 14, 'Appointment', 4, 1500, 'Success', '2026-01-10 21:29:38', '2026-01-10 21:29:38'),
(5, 6, 6, 'Appointment', 5, 1500, 'Success', '2026-01-10 21:32:08', '2026-01-10 21:32:08'),
(6, 6, 15, 'Appointment', 6, 1000, 'Success', '2026-01-10 21:33:40', '2026-01-10 21:33:40'),
(32, 3, 2, 'Appointment', 18, 1500, 'Success', '2026-01-31 14:03:04', '2026-01-31 14:03:04'),
(8, 3, 8, 'Appointment', 8, 2000, 'Success', '2026-01-10 21:36:58', '2026-01-11 22:38:35'),
(9, 3, 4, 'Appointment', 9, 1500, 'Success', '2026-01-10 21:40:07', '2026-01-12 09:32:06'),
(10, 4, 11, 'Appointment', 10, 1500, 'Success', '2026-01-10 21:42:54', '2026-01-11 22:37:16'),
(11, 4, 1, 'Appointment', 11, 1000, 'Success', '2026-01-10 21:44:21', '2026-01-10 21:44:21'),
(12, 4, 7, 'Appointment', 12, 2000, 'Success', '2026-01-10 21:47:36', '2026-01-10 21:47:36'),
(13, 5, 3, 'Appointment', 13, 1000, 'Success', '2026-01-10 21:59:39', '2026-01-10 21:59:39'),
(14, 5, 12, 'Appointment', 14, 1500, 'Success', '2026-01-10 22:03:17', '2026-01-10 22:03:17'),
(15, 5, 13, 'Appointment', 15, 2000, 'Success', '2026-01-10 22:06:30', '2026-01-10 22:06:30'),
(16, 1, 5, 'Appointment', 16, 1000, 'Success', '2026-01-10 22:12:27', '2026-01-10 22:12:27'),
(17, 1, 16, 'Appointment', 17, 1000, 'Success', '2026-01-10 22:14:12', '2026-01-10 22:14:12'),
(18, 4, 1, 'Consult', 1, 2000, 'Success', '2026-01-10 22:20:42', '2026-01-10 22:21:57'),
(19, 3, 2, 'Consult', 2, 2500, 'Failed', '2026-01-10 22:24:19', '2026-01-10 22:24:19'),
(20, 5, 3, 'Consult', 3, 1700, 'Failed', '2026-01-11 22:08:35', '2026-01-11 22:08:35'),
(21, 6, 6, 'Consult', 4, 1550, 'Failed', '2026-01-11 22:12:40', '2026-01-11 22:12:40'),
(22, 2, 9, 'Consult', 5, 1370, 'Failed', '2026-01-11 22:17:22', '2026-01-11 22:17:22'),
(23, 4, 11, 'Consult', 6, 1420, 'Failed', '2026-01-11 22:23:14', '2026-01-11 22:23:14'),
(24, 5, 12, 'Consult', 7, 1610, 'Failed', '2026-01-11 22:25:21', '2026-01-11 22:25:21'),
(25, 5, 13, 'Consult', 8, 2000, 'Success', '2026-01-11 22:27:56', '2026-01-11 22:38:35'),
(26, 5, 13, 'Consult', 9, 2000, 'Success', '2026-01-11 22:28:16', '2026-01-12 09:32:06'),
(27, 2, 14, 'Consult', 10, 1840, 'Success', '2026-01-11 22:30:53', '2026-01-11 22:37:16'),
(28, 1, 16, 'Consult', 11, 1800, 'Failed', '2026-01-11 22:33:25', '2026-01-11 22:33:25'),
(29, 5, 13, 'Consult', 12, 1500, 'Failed', '2026-01-12 09:30:10', '2026-01-12 09:30:10'),
(30, 6, 16, 'Appointment', 18, 1000, 'Success', '2026-01-27 12:03:26', '2026-01-27 12:03:26'),
(33, 3, 2, 'Consult', 12, 1370, 'Failed', '2026-01-31 14:04:19', '2026-01-31 14:04:19'),
(35, 6, 6, 'Consult', 12, 2500, 'Failed', '2026-02-02 20:52:44', '2026-02-02 20:52:44'),
(36, 4, 11, 'Consult', 13, 2000, 'Failed', '2026-03-11 23:45:17', '2026-03-11 23:45:17'),
(37, 3, 11, 'Appointment', 20, 1500, 'Success', '2026-03-12 10:16:50', '2026-03-12 10:16:50'),
(38, 6, 11, 'Appointment', 21, 1500, 'Success', '2026-03-12 10:22:58', '2026-03-12 10:22:58'),
(39, 6, 16, 'Appointment', 22, 1000, 'Success', '2026-03-21 15:40:32', '2026-03-21 15:40:32'),
(40, 6, 16, 'Appointment', 23, 1000, 'Success', '2026-03-21 15:42:03', '2026-03-21 15:42:03'),
(41, 1, 6, 'Appointment', 24, 1500, 'Success', '2026-03-24 14:06:54', '2026-03-24 14:06:54');

-- --------------------------------------------------------

--
-- Table structure for table `specialization_tb`
--

DROP TABLE IF EXISTS `specialization_tb`;
CREATE TABLE IF NOT EXISTS `specialization_tb` (
  `s_id` int(11) NOT NULL AUTO_INCREMENT,
  `s_name` varchar(50) NOT NULL,
  `s_image` varchar(100) NOT NULL,
  `s_status` enum('Active','Deactive') NOT NULL,
  `s_cdate` datetime NOT NULL,
  `s_udate` datetime NOT NULL,
  PRIMARY KEY (`s_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `specialization_tb`
--

INSERT INTO `specialization_tb` (`s_id`, `s_name`, `s_image`, `s_status`, `s_cdate`, `s_udate`) VALUES
(1, 'Endocrinologist', 'Endocrinologist.jpeg', 'Active', '2025-10-17 00:00:00', '2025-12-29 20:48:09'),
(2, 'Gynaecologist', 'gyn_qNm5JwJ.jpg', 'Active', '2025-11-03 10:34:00', '2025-12-31 13:18:54'),
(3, 'Nephrology', 'nephrologist_LTFnxxN.jpeg.jpg', 'Active', '2025-11-26 09:09:26', '2025-12-31 13:18:30'),
(4, 'Dermatologist', 'derma.jpg', 'Active', '2025-11-03 12:45:55', '2025-12-31 13:22:09'),
(5, 'Pediatric', 'pediatician.jpg', 'Active', '2025-11-26 22:58:55', '2025-12-31 13:17:04'),
(6, 'Dietitian', 'dietician.jpg', 'Active', '2025-12-29 20:49:00', '2025-12-31 13:17:40'),
(7, 'Pulmonologist', 'pulmonologist_cxbtXO5.jpg', 'Active', '2025-12-29 20:49:29', '2025-12-31 13:15:55'),
(8, 'Sports Nutritionist', 'sports.jpg', 'Active', '2025-12-29 20:50:20', '2025-12-31 13:15:35');

-- --------------------------------------------------------

--
-- Table structure for table `user_tb`
--

DROP TABLE IF EXISTS `user_tb`;
CREATE TABLE IF NOT EXISTS `user_tb` (
  `u_id` int(11) NOT NULL AUTO_INCREMENT,
  `u_name` varchar(20) NOT NULL,
  `u_contact` bigint(20) NOT NULL,
  `u_address` text NOT NULL,
  `u_gender` enum('Male','Female','Other') NOT NULL,
  `u_image` varchar(100) NOT NULL,
  `u_dob` date NOT NULL,
  `u_bloodgroup` varchar(10) NOT NULL,
  `u_password` varchar(20) NOT NULL,
  `u_status` enum('Active','Deactive') NOT NULL,
  `u_cdate` datetime NOT NULL,
  `u_udate` datetime NOT NULL,
  PRIMARY KEY (`u_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_tb`
--

INSERT INTO `user_tb` (`u_id`, `u_name`, `u_contact`, `u_address`, `u_gender`, `u_image`, `u_dob`, `u_bloodgroup`, `u_password`, `u_status`, `u_cdate`, `u_udate`) VALUES
(1, 'Urvashi Chavada', 9016303552, 'Reception, CLUB HOUSE, Sardar Patel Ring Rd, near Bopal, Crossing, Bopal, Ahmedabad, Gujarat 380058', 'Female', 'urvshi_6AdctI6.jpg', '2005-11-18', 'A-', '12345', 'Active', '2025-12-22 21:25:21', '2026-03-24 14:38:43'),
(2, 'Palak Raval', 8799271334, 'Plot 35/1, sector 2 A, near swaminarayan narayan temple, Gandhinagar, Gujarat 382007', 'Female', 'palak_YyzBhKH.jpg', '2006-03-15', 'A+', '12345', 'Active', '2025-12-25 20:39:42', '2026-01-11 22:37:28'),
(3, 'Navneet Kaur', 9991935129, '38, Green Villa Complex, Near HB Kapadiya School Road, Gurukul Rd, Memnagar, Ahmedabad, Gujarat 380052', 'Female', 'navneet_yiiWa4v.jpg', '2006-05-27', 'AB+', '12345', 'Active', '2025-12-25 21:06:42', '2026-03-12 10:19:58'),
(4, 'Raj Chavda', 7201041745, 'Iris Hospital, Lambhvel Rd, Patel Chokdi, Vivekanand Wadi, Anand, Gujarat 388001', 'Male', 'Raj.jpeg', '2006-01-23', 'B+', '12345', 'Active', '2025-12-25 21:16:20', '2026-03-11 23:26:41'),
(5, 'Pratik Raval', 7096996399, 'Ground Floor, Universal Hospital, Ring Rd, near Kiran Motors, Jariwala Compound, Khatodra Wadi, Surat, Gujarat 395002', 'Male', 'Pratik.jpeg', '2006-07-23', 'AB-', '12345', 'Active', '2025-12-25 22:29:08', '2026-01-10 22:09:23'),
(6, 'Komal Patel', 9723001502, 'Plot No-1285, Sector-6 D, Near, GH 3 Cir, opposite Civil Hospital, Gandhinagar, Gujarat 382006', 'Male', 'Komal.jpeg', '2006-01-23', 'A+', '12345', 'Active', '2025-12-29 16:20:18', '2026-03-24 13:57:44'),
(7, 'urvashi Chavda', 9016303552, 'Plot 35/1, sector 2 A, near swaminarayan narayan temple, Gandhinagar, Gujarat 382007.', 'Female', 'n7_RqVCFNS.jpg', '2005-11-18', 'A-', '12345', 'Active', '2026-03-11 23:09:47', '2026-03-11 23:13:45');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
