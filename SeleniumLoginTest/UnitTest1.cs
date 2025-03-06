using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support.UI;
using SeleniumExtras.WaitHelpers;
using System;
using System.Collections.ObjectModel;
using System.IO;

namespace SeleniumLoginTest
{
    public class Tests
    {
        private ChromeDriver driver;
        private WebDriverWait wait;
        private string tempUserDataDir;

        [SetUp]
        public void Setup()
        {
            tempUserDataDir = Path.Combine(Path.GetTempPath(), Path.GetRandomFileName());
            Directory.CreateDirectory(tempUserDataDir);

            ChromeOptions options = new ChromeOptions();
            options.AddArgument($"--user-data-dir={tempUserDataDir}");

            driver = new ChromeDriver(options);
            wait = new WebDriverWait(driver, TimeSpan.FromSeconds(10));

            driver.Navigate().GoToUrl("https://practicetestautomation.com/practice-test-login/");
        }

        [TearDown]
        public void TearDown()
        {
            if (driver != null)
            {
                driver.Quit();
                driver = null;
            }
            Directory.Delete(tempUserDataDir, true);
        }

        [Test]
        public void TestLoginSuccess()
        {
            IWebElement usernameField = wait.Until(ExpectedConditions.ElementIsVisible(By.Id("username")));
            IWebElement passwordField = wait.Until(ExpectedConditions.ElementIsVisible(By.Id("password")));
            IWebElement loginButton = wait.Until(ExpectedConditions.ElementToBeClickable(By.Id("submit")));

            usernameField.SendKeys("student");
            passwordField.SendKeys("Password123");
            loginButton.Click();

            IWebElement successMessage = wait.Until(ExpectedConditions.ElementIsVisible(By.XPath("//h1[contains(text(), 'Logged In Successfully')]")));
            Assert.IsTrue(successMessage.Displayed, "Login successful: Success message displayed");
        }

        [Test]
        public void TestLoginFailureInvalidCredentials()
        {
            IWebElement usernameField = wait.Until(ExpectedConditions.ElementIsVisible(By.Id("username")));
            IWebElement passwordField = wait.Until(ExpectedConditions.ElementIsVisible(By.Id("password")));
            IWebElement loginButton = wait.Until(ExpectedConditions.ElementToBeClickable(By.Id("submit")));

            usernameField.SendKeys("invalid_user");
            passwordField.SendKeys("invalid_password");
            loginButton.Click();

            try
            {
                ReadOnlyCollection<IWebElement> errorElements = wait.Until(ExpectedConditions.VisibilityOfAllElementsLocatedBy(By.Id("error")));
                IWebElement errorElement = errorElements.ElementAtOrDefault(0);

                if (errorElement != null)
                {
                    Assert.IsTrue(errorElement.Displayed, "Login failed: Error element displayed");
                }
                else
                {
                    Assert.Fail("No error element found.");
                }
            }
            catch (WebDriverTimeoutException ex)
            {
                Assert.Fail($"Error element was not visible. Exception: {ex.Message}");
            }
        }
    }
}