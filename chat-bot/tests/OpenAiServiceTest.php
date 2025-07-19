<?php
declare(strict_types=1);

namespace App\Tests\Service;

use PHPUnit\Framework\TestCase;
use App\Service\OpenAiService;

final class OpenAiServiceTest extends TestCase
{
    private const DUMMY_KEY = 'sk-FAKEKEY';

    public function testConstructEmptyKeyThrows(): void
    {
        $this->expectException(\InvalidArgumentException::class);
        new OpenAiService('');
    }

    public function testAskEmptyQuestionThrows(): void
    {
        $service = new OpenAiService(self::DUMMY_KEY);
        $this->expectException(\InvalidArgumentException::class);
        $service->ask('   ');
    }

    public function testInvalidJsonThrowsRuntimeException(): void
    {
        $mock = $this->getMockBuilder(OpenAiService::class)
                     ->setConstructorArgs([self::DUMMY_KEY])
                     ->onlyMethods(['sendRequest'])
                     ->getMock();

        $mock->method('sendRequest')
             ->willReturn('not a json');

        $this->expectException(\RuntimeException::class);
        $this->expectExceptionMessage('Invalid JSON response');
        $mock->ask('Hello');
    }
}
