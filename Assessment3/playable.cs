//Interface Implementation Challenge**

using System;

// Define an interface `IPlayable` with a method `Play()`.
public interface IPlayable
{
    void Play();
}

// Implement this interface in `MusicPlayer` class with a specific implementation.
public class MusicPlayer : IPlayable
{
    public void Play()
    {
        Console.WriteLine("Playing music...");
    }
}

// Implement this interface in `VideoPlayer` class with a specific implementation.
public class VideoPlayer : IPlayable
{
    public void Play()
    {
        Console.WriteLine("Playing video...");
    }
}

// Main method to demonstrate the functionality
public class Program1
{
    public static void Main(string[] args)
    {
        IPlayable musicPlayer = new MusicPlayer();
        IPlayable videoPlayer = new VideoPlayer();

        musicPlayer.Play();
        videoPlayer.Play();
    }
}
