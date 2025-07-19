<?php
declare(strict_types=1);

namespace App\Tests\Controller;

use PHPUnit\Framework\TestCase;
use App\Controller\ChatController;
use App\Service\OpenAiService;

final class ChatControllerTest extends TestCase
{
    public function testEmptyQuestionDisplaysError(): void
    {
        $_SERVER['REQUEST_METHOD'] = 'POST';
        $_POST['question'] = '  ';

        $service = $this->getMockBuilder(OpenAiService::class)
                        ->disableOriginalConstructor()
                        ->getMock();

        ob_start();
        (new ChatController($service))->handle();
        $output = ob_get_clean();

        $this->assertStringContainsString('Please enter a question.', $output);
    }

    public function testValidQuestionDisplaysAnswer(): void
    {
        $_SERVER['REQUEST_METHOD'] = 'POST';
        $_POST['question'] = 'How are you?';

        $service = $this->getMockBuilder(OpenAiService::class)
                        ->disableOriginalConstructor()
                        ->getMock();
        $service->method('ask')
                ->with('How are you?')
                ->willReturn('I am fine.');

        ob_start();
        (new ChatController($service))->handle();
        $output = ob_get_clean();

        $this->assertStringContainsString('I am fine.', $output);
    }
}
